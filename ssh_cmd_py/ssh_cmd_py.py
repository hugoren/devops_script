#!/usr/bin/env python
#conding:utf-8

import paramiko ,threading,sys,subprocess


class ssh_client(threading.Thread):


    def __init__(self,ip,username,password,commands):
        threading.Thread.__init__(self)
        self.ip = ip
        self.username = username
        self.password = password
        self.commands = commands


    def ssh_exce_cmd(self):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.ip,22,self.username,self.password,timeout=5)
            for command in self.commands:
                stdin,stdout,stderr = ssh.exec_command(command)
                # return_code = ssh.subprocess.Popen('echo "90909" >>/Users/hugo/test.txt', shell=True)
            stdin.write("Y")
            print stdout.read()
            # print return_code
            ssh.close()
        except:
            print '%s ip ssh err'%(ip)


if __name__ == '__main__':
    ip = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    command_list = open('command_list','r')
    commands = []
    # threads = []
    for each_command in command_list:
        commands.append(each_command)
        temp_thread = ssh_client(ip,username,password,commands)
        # threads.append(temp_thread.ssh_exce_cmd())
    threading.Thread(temp_thread.ssh_exce_cmd()).start()
