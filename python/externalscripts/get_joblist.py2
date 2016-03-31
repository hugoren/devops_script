#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import zookeeper
import json


def get_job_list(zk):
    root_list = zookeeper.get_children(zk, '/')
    job_list = {}
    job_list['data'] = []

    for root in root_list:
        if root == "zookeeper":
	    continue
        job_name = zookeeper.get_children(zk, '/' + root)
        for job in job_name:
            temp = {'{#JOBPATH}':"/%s/%s" % (root,job)}
            job_list['data'].append(temp)
    job_list_json = json.dumps(job_list, indent=4, sort_keys=True)
    print job_list_json


def main():
    zk_server = "10.232.71.108:2181,10.221.224.131:2181,10.104.145.101:2181"
    zookeeper.set_debug_level(zookeeper.LOG_LEVEL_ERROR)
    try:
        zk = zookeeper.init(zk_server)
        get_job_list(zk)
    except Exception, e:
        print "Create zookeeper session Failed:%s" % e

if __name__ == "__main__":
    main()

