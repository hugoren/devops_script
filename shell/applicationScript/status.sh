#!/bin/sh


function status(){
     #echo ${var:0-7}
     #表示从右边第七个字符开始，一直到结束。    
     for ((i=0;i<6;i++))
     do
        sleep 10
        returnWasValue=`wget -T 120 "${DETECTION_APP}${MOBILE_HTPP_PARAMETER}" --spider 2>&1 | grep "HTTP" |grep -n 'K\{1\}'`
        if [ "${returnWasValue:0-2}" = "OK" ];then
               echo "${APP} publish successful"
               exit 0
        else
               ((j++))
               if [ $j -ge 6 ];then {
                   echo "${APP} can't visit. Please check the reasons"
                   exit 1
                }
                else
                   echo "this the $j repeated"
                fi

        fi
    done
}
~
