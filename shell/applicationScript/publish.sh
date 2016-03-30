#!/bin/sh
function publish(){

        cd ${APP_PATH}
        #Delete the old package, and copy the latest from package 

        if [ -f ${APP}-1.0-SNAPSHOT.tgz2* ];then
                mv ${APP}-1.0-SNAPSHOT.tgz2* ./bak/
        fi
        
        if [  -f "${APP}-1.0-SNAPSHOT.tgz" ];then
            cp -r ${APP}-1.0-SNAPSHOT.tgz{,$UP_TIME}
            rm -fr ${APP}-1.0-SNAPSHOT.tgz
            rm -fr ${APP}-1.0-SNAPSHOT
        else
            rm -fr ${APP}-1.0-SNAPSHOT.tgz
            rm -fr ${APP}-1.0-SNAPSHOT
        fi
        
        cp -r ${CP_PACKAGE}/${APP}-1.0-SNAPSHOT.tgz  ./
        tar  -xvf ${APP}-1.0-SNAPSHOT.tgz
}
