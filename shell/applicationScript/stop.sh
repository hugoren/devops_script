#!/bin/sh
   if [ $# -eq 1 ];then
      APP_NAME=$1
      ps -ef|grep ${APP_NAME}-1.0-SNAPSHOT|grep -v grep |awk '{print $2}'|xargs kill -9 
   else
       ps -ef|grep ${APP}-1.0-SNAPSHOT|grep -v grep |awk '{print $2}'|xargs kill -9 
   fi
