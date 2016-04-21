#!/usr/bin/env bash

app=$1

pid_file=${publish_path}/${app}/RUNNING_PID


if [ ! -f ${pid_file} ];then
    echo "$app is not running."
    exit 5
fi

function stop() {
    for ((i=0;i<3;i++))
    do
       kill -9 ${pid}
       if [ $? -eq 0 ];then
              rm -f ${pid_file}
              exit 0
       else
           sleep 5
           continue
       fi
    done
    exit 6
}


pid=`cat ${pid_file}`
stop

