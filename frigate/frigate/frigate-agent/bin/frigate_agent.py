#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from subprocess import Popen, PIPE, check_output
from argparse import ArgumentParser
from ConfigParser import ConfigParser
from getpass import getuser
import  pack_download_client 
import sys
import os
import urllib2
import tarfile
import time
import shutil


# 读取配置文件
def read_conf(conf="../conf/agent.conf"):
    config = ConfigParser()
    config.read(conf)
    all_config = {}
 
    for section in config.sections():
        all_config[section] = {}
        for key, value in config.items(section):
            all_config[section][key] = value

    config = all_config["default"]
    all_config.pop("default")
    env = all_config["env"]
    all_config.pop("env")

    return config, env, all_config


# 运行后台命令,如启动进程
def run_command_background(app, command, env, app_ops):
    all_env = {}

    for k, v in env.items():
        all_env[k] = v

    for k, v in app_ops.items():
        all_env[k] = v

    process = Popen(command, shell=True, env=all_env)
    time.sleep(10)
    pid = check_output("ps aux | grep %s | grep -v grep| grep -v frigate| awk '{print $2}'" % app, shell=True)
    if len(pid.strip()) == 0:
        print "%s启动失败,未找到进程." % app
        sys.exit(12)
    else:
        print "启动成功,PID为%s" % pid



# 运行命令,会判断返回值和输出
def run_command(command, env):
    process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE, env=env)
    output, error = process.communicate()

    if process.returncode != 0:
        print "标准输出:"
        print output
        print "错误输出:"
        print error
        print "执行结果:失败."
    else:
        print "标准输出:"
        print output
        print "执行结果:成功."


# 进程的启停
def service(app, port, action, base_dir, env, app_ops, check_url):
    start_sh = "%s/libs/start.sh" % base_dir
    stop_sh = "%s/libs/stop.sh" % base_dir

    start_app = "%s %s" % (start_sh, app)
    stop_app = "%s %s" % (stop_sh, app)

    if action == "start":
        print "-" * 60
        print "启动 %s . . ." % app
        run_command_background(app, start_app, env, app_ops)
        check(app, port, check_url)
    elif action == "stop":
        print "-" * 60
        print "停止 %s . . ." % app
        run_command(stop_app, env)
    elif action == "restart":
        print "-" * 60
        print "停止 %s ..." % app
        run_command(stop_app, env)
        print "-" * 60
        print "启动 %s . . ." % app
        run_command_background(app, start_app, env, app_ops)
        check(app, port, check_url)
    else:
        print "frigate_agent -s start/stop/restart APP."


def download(app, pkg_path, pub_version, environment):
    print "-" * 60
    print "开始下载%s程序文件" % app

    # 调用app_repo api下载
    if pub_version == "stable":
        pkg_tag = "%s_%s_snapshot_.tgz" % (environment, app)
        pack_download_client.download_file(pkg_path, pkg_tag)
    else:
        pack_download_client.download_file(pkg_path, pub_version)

    # 通过web方式下载
    #repo_url = "http://127.0.0.1/%s.tgz" % app

    #f = urllib2.urlopen(repo_url)
    #data = f.read()
    #with open("%s/%s.tgz" % (pkg_path, app), "wb") as code:
    #    code.write(data)

# 备份老版本程序
def backup(app, publish_path, back_path):
    print "-" * 60
    print "备份%s ..." % app,
    ensure_dir_exist(back_path)
    back_file_name = "%s/%s_%s.tgz" % (back_path, app, time.strftime("%Y%m%d_%H%M", time.localtime()))
    try:
        back_tar = tarfile.open(back_file_name, "w:gz")
        back_tar.add("%s/%s" %(publish_path, app), arcname=app)
        print "成功."
    except Exception , e:
        print "失败."
        print "错误信息:%s" % e
        return None


# 发布程序
def publish(app, pkg_path, publish_path, is_backup, backup_path, pub_version, environment):

    if is_backup:
        backup(app, publish_path, backup_path)

    download(app, pkg_path, pub_version, environment)
    print "-" * 60
    print "发布%s到程序目录" % app

    full_name = "%s/%s.tgz" %(pkg_path, app)
    try:
        tar = tarfile.open(full_name, "r:gz")
        tar.extractall(publish_path)
    except Exception, e:
        print e


# 应用健康检查
def check(app, port, check_url):
    check_url = "http://127.0.0.1:%s%s" % (port, check_url)
    print "-" * 60
    print "开始测活,测活地址为:%s" %check_url

    for i in range(1, 7):
        print "正在进行%s的第%d次测活 ..." % (app, i)
        try:
            response  = urllib2.urlopen(check_url)
            http_code = response.getcode()
            if http_code == 200:
                print "%s 程序测活正常." % app
                break
            else:
                print "%s 程序测活失败,http返回码为%s" % (app, http_code)
        except Exception, e:
            print "%s 测活失败,无法连接测活地址." % app
            print "错误信息:%s" % e
        time.sleep(10)


# 确保目录存在
def ensure_dir_exist(path):
    if not os.path.exists(path):
        os.makedirs(path)


# 读取调用参数
def argparse():
    parser = ArgumentParser(description="start/stop/restart or publish app.")
    group = parser.add_mutually_exclusive_group()

    group.add_argument("-s", "--server", dest="ACTION", action='store', default='', help="启动/停止/重启应用.")
    group.add_argument("-p", "--publish", dest="VERSION", action='store', default='', help="发布/回滚应用.")
    parser.add_argument("-b", "--backup", action='store_true', help="发布前进行否备份.")
    parser.add_argument("app", action='store', help="应用名称.")

    given_args = parser.parse_args()

    return given_args


# 主程序
def main():
    config_file = "/data/xingren_share/applicationScript/frigate-agent/conf/agent.conf"

    #检查配置文件是否存在
    if not os.path.exists(config_file):
        print "配置文件不存在."
        sys.exit(9)

    if getuser() == "root":
        print "请不要使用root用户运行."
        sys.exit(10)

    config, env, all_app_ops = read_conf(conf=config_file)
    given_args = argparse()

    # 通过命令行读取的参数
    app = given_args.app
    action = given_args.ACTION
    pub_version = given_args.VERSION
    is_backup = given_args.backup

    # 从配置配置文件读取参数
    pkg_path = "%s/%s" % (config["pkg_dir"], app)
    publish_path = config["publish_dir"]
    backup_path = "%s/%s" % (config["back_dir"], app)
    base_dir = config["base_dir"]
    environment = config["environment"]


    if app in all_app_ops.keys():
        app_ops = all_app_ops[app]
        port = app_ops["http_port"]
        if app_ops.has_key("check_url"):
            check_url = app_ops["check_url"]
        else:
            check_url = ""

        ensure_dir_exist(pkg_path)
        ensure_dir_exist(publish_path)
        ensure_dir_exist("/data/logs/gc")

        if len(action) != 0:
            # 进行服务器的启停/重启操作
            service(app, port, action, base_dir, env, app_ops, check_url)
        elif len(pub_version) != 0:
            # 服务的发布,是否备份,发布哪个版本都在publish内部实现
            service(app, port, "stop", base_dir, env, app_ops, check_url)
            publish(app, pkg_path, publish_path, is_backup, backup_path, pub_version, environment)
            service(app, port, "start", base_dir, env, app_ops, check_url)
        else:
            check(app, port, check_url)
    else:
        print "没有找到%s的配置.程序退出." % app
        sys.exit(4)


if __name__ == "__main__":
    main()
