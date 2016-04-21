#!/bin/bash


app=$1

source /etc/profile
source /etc/bashrc

function start(){
#    echo "${publish_path}/${app}/bin/${app} -Dhttp.port=${http_port} -Dhttps.port=${https_port} -Djava.awt.headless=true \
#    -Dfile.encoding=UTF-8 \
#    -J-javaagent:${oneapm} -J-javaagent:${kamon} -J-server -J-XX:+UseConcMarkSweepGC -J-Xms${jxms} -J-Xmx${jxmx} \
#    -J-XX:NewSize=${new_size} -J-XX:MaxNewSize=${max_new_size} -J-XX:PermSize=${perm_size} -J-XX:+ScavengeBeforeFullGC \
#    -J-XX:+CMSScavengeBeforeRemark -J-d64 -J-XX:+UseCompressedOops -J-XX:+PrintGC -J-XX:+PrintGCDetails \
#    -J-XX:+PrintGCTimeStamps -J-XX:+PrintHeapAtGC -J-XX:+PrintTenuringDistribution \
#    -J-Xloggc:/data/logs/gc/${app}.log -J-XX:+HeapDumpOnOutOfMemoryError \
#    -J-XX:HeapDumpPath=/data/logs/dump.hprof > /data/logs/${app}.log 2>&1 &"

    jvm_ops="-Dhttp.port=${http_port} -Djava.awt.headless=true -Dfile.encoding=UTF-8 -J-javaagent:${kamon} -J-javaagent:${oneapm} -J-server -J-XX:+UseConcMarkSweepGC -J-Xms${jxms} -J-Xmx${jxmx} -J-XX:NewSize=${new_size} -J-XX:MaxNewSize=${max_new_size} -J-XX:PermSize=${perm_size} -J-XX:+ScavengeBeforeFullGC -J-XX:+CMSScavengeBeforeRemark -J-d64 -J-XX:+UseCompressedOops -J-XX:+PrintGC -J-XX:+PrintGCDetails -J-XX:+PrintGCTimeStamps -J-XX:+PrintHeapAtGC -J-XX:+PrintTenuringDistribution -J-Xloggc:/data/logs/gc/${app}.log -J-XX:+HeapDumpOnOutOfMemoryError -J-XX:HeapDumpPath=/data/logs/dump.hprof"
    if [ `echo $https_port | wc -c | tr -d " "` -gt 1 ];then
        jvm_ops="-Dhttps.port=${https_port} $jvm_ops"
    fi

    `${publish_path}/${app}/bin/${app} ${jvm_ops} > /data/logs/${app}.log 2>&1 &` 

}

start
