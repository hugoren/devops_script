#!/usr/bin/env python
#conding:utf-8

import paramiko ,threading,sys,subprocess

ip = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
app = sys.argv[4]
# cmd = sys.argv[4]
command_list = open('command_list','r')
commands =[]
for each_command in command_list:
    commands.append(each_command)
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
        for command in commands:
            stdin,stdout,stderr = ssh.exec_command(command)
        # return_code = ssh.subprocess.Popen('echo "90909" >>/Users/hugo/test.txt', shell=True)
        stdin.write("Y")
        print stdout.read()
        # print return_code
        ssh.close()
    except:
        print '%s ip ssh err'%(ip)

if __name__ == '__main__':
    # cmd = ['cd /data','cd /data & touch t9.txt']
    # ip = "119.29.101.41"
    # username = "admin"
    # password = "y298FTgS8Y"
    # threads = [5]
    ssh_cmd()