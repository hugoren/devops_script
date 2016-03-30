#!/bin/sh

function rollback(){

        cd ${APP_PATH}
        if [  -d "${APP}-1.0-SNAPSHOT" ];then
               rm -fr ${APP}-1.0-SNAPSHOT
               rm -fr ${APP}-1.0-SNAPSHOT.tgz
               tar  -zxvf ${APP}-1.0-SNAPSHOT.tgz20*     
        else
               tar  -zxvf ${APP}-1.0-SNAPSHOT.tgz20*
        fi
}
