#!/usr/bin/env python
#conding:utf-8

import paramiko ,threading,sys,subprocess

ip = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
app_name = sys.argv[4]
#app = sys.argv[4]
# cmd = sys.argv[4]
#command_list = open('/data/monitor/zabbix/share/zabbix/externalscripts/command_list','r')
#commands =[]
#for each_command in command_list:
#    commands.append(each_command)
# cmd = ["cd /data","touch t9.txt"]
# def ssh_cmd(ip,username,password,cmd):
def ssh_cmd():
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,password,timeout=5)
        # for m in cmd:
        #     stdin,stdout,stderr = ssh.exec_command(m)
        #     stdin.write("Y")
        #     out = stdout.readlines()
        #     for o in out:
        #         print o
        #     print  '%s\tOK\n'%(ip)
        # stdin,stdout,stderr = ssh.exec_command("cd /data & touch t9.txt")
        #for command in commands:
        #print commands
        stdin,stdout,stderr = ssh.exec_command("echo `ps -ef|grep %s |grep -v grep |awk '{print $2}'`"%app_name)
        # return_code = ssh.subprocess.Popen('echo "90909" >>/Users/hugo/test.txt', shell=True)
        stdin.write("Y")
        #print stdout.read()
        # print return_code
        if  len(stdout.read()) < 2:

        #        # print stdout.read()
                print  -1
        else:
                print 1
        ssh.close()
    except Exception as e:
        print e.message

if __name__ == '__main__':
    # cmd = ['cd /data','cd /data & touch t9.txt']
    # ip = "119.29.101.41"
    # username = "admin"
    # password = "y298FTgS8Y"
    # threads = [5]
    ssh_cmd()
