#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import zookeeper
import argparse
import sys


def get_znode(zk, path):
    for i in range(3):
        try:
            result = zookeeper.get(zk,path)
            return result
        except zookeeper.NoNodeException:
            return False
        except zookeeper.ConnectionLossException:
            continue


def get_children_node(zk,path):
    try:
        children = zookeeper.get_children(zk,path)
    except Exception, e:
        print "Get children node error:%s" %e
    return children


def check_server_status(zk,root_path):
    path_server_list = root_path+"/servers"
    server_list = get_children_node(zk,path_server_list)
    alert = "false"
    for i in server_list:
        path_server_status = path_server_list + "/%s/status" %i
        server_status = get_znode(zk,path_server_status)[0]
        print i+":",
        if server_status == "READY" or server_status == "RUNNING":
            print "OK",
        else:
            print "ERROR"
            alert = "true"
    print "alert:"+alert


def check_jobs_status(zk,root_path):
    path_job_status = root_path+"/execution/0/completed"
    path_job_running = root_path+"/execution/0/running"
    if get_znode(zk,path_job_running):
        print "0"
    else:
        if get_znode(zk,path_job_status):
            print "0"
        else:
            print "0"


def get_job_runtime(zk,root_path):
    path_begin = root_path + "/execution/0/lastBeginTime"
    path_complete = root_path + "/execution/0/lastCompleteTime"
    begin_time = get_znode(zk,path_begin)[0]
    complete_time = get_znode(zk,path_complete)[0]
    runtime = int(complete_time) - int(begin_time)
    print runtime


def opt_parser():
    parser = argparse.ArgumentParser(description="Get job status.")
    parser.add_argument('-j',action='store',dest='root_path',type=str,required=True,help="job root path (ex:'/web/PushStatus')")
    parser.add_argument('-a',action='store',dest='action',type=str,required=True,help="what to do(ex:'job_status' to get job status,'server-status' to get server status,'job_runtime' to get last job run time)")
    given_args = parser.parse_args()
    return given_args


def main():
    given_args = opt_parser()
    server = '10.232.71.108:2181,10.221.224.131:2181,10.104.145.101:2181'
    root_path = given_args.root_path
    action =  given_args.action
    zookeeper.set_debug_level(zookeeper.LOG_LEVEL_ERROR)
    try:
        zk = zookeeper.init(server)
    except Exception, e:
        print "Create zookeeper session Failed:%s" %e
    if action == "job_status":
        check_jobs_status(zk,root_path)
    elif action == "job_runtime":
        get_job_runtime(zk,root_path)
    elif action == "server_status":
        check_server_status(zk,root_path)
    else:
        print "only 3 accepted actions:job_status,server-status,runtime"
        zookeeper.close(zk)
        sys.exit(0)
    zookeeper.close(zk)

if __name__ == '__main__':
    main()


