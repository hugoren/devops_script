#!/bin/sh

#解压
function ungz(){
   cd  /data/nginx/logs/
   for i in access*.gz ;do
      gunzip –c access*.gz >> acccessXX.log 
   done
｝


#先按关键字统计ip，再统计一天内ip最高到低排序
function tongji_ip(){
    cd /data/nginx/yisheng2_tongji
    for i in *;
    do
      cat $i |grep -w "/home"|sed "s/.* \([0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\).*/\1/;s/[^0-9 ]*\([0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\).*/\1/"| sort | uniq -c | sort -k1,1nr  >>/data/nginx/yisheng2_tongji/$i.txt
    done

}

ungz()
tongji_ip()
