#!/bin/bash

#应用私有的变量
    APP=admin
    HTTP_PORT=
    HTTPS_PORT=
    JXMS=3000M
    JXMX=3000m
    NEW_SIZE=700M
    MAX_NEW_SIZE=700M
    PERM_SIZE=512m

#应用引入公共变量
    source /data/_share/applicationScript/config

#检测应用启动时是否加载参数
   if [ $# -eq 0 ];then
       echo "please input parameter"
       exit 1
    fi

#前面只是引用逻辑，在这才是真的启动应用
    function startup(){
         ps -ef|grep ${APP}-1.0-SNAPSHOT|grep -v grep |awk '{print $2}'|xargs kill -9  

}

#根据不同的应用，应用健康状态检测的参数不同
   if [ ${APP}x = "mobile"x  ];then
         MOBILE_HTPP_PARAMETER="/api/config/title"
     else
         MOBILE_HTPP_PARAMETER=""
   fi

#根据参数执行不同的功能
   if [ $# -eq 2 ];then
       source ${SHELL_PATH}/$1
       source ${SHELL_PATH}/$2
       #去掉后缀，获取函数的方法名
       parameter1=$1
       parameter2=$2
       ${parameter1%.*}
       startup
       ${parameter2%.*}
    fi

    if [ $# -eq 3 ];then
       source ${SHELL_PATH}/$1
       source ${SHELL_PATH}/$2
       source ${SHELL_PATH}/$3
       #去掉后缀，获取函数的方法名
       parameter1=$1
       parameter2=$2
       parameter3=$3
       ${parameter1%.*}
       ${parameter2%.*}
       startup
       ${parameter3%.*}
     fi
