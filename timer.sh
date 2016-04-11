#!/bin/sh
test=$1
timer=$2
sleeper=$3
ex_timer=$4

>time.txt
# arg1=start, arg2=end, format: %s.%N  
function getTiming() {  
    start=$1  
    end=$2  
     
    start_s=$(echo $start | cut -d '.' -f 1)  
    start_ns=$(echo $start | cut -d '.' -f 2)  
    end_s=$(echo $end | cut -d '.' -f 1)  
    end_ns=$(echo $end | cut -d '.' -f 2)  
    time=$(( ( 10#$end_s - 10#$start_s ) * 1000 + ( 10#$end_ns / 1000000 - 10#$start_ns / 1000000 ) ))  
    echo "$time ms"  >> time.txt 
}  
  
for((i=1;i<=${timer};i++));do
    #shuzu=(30 50 70 90 110)
    #for j in ${shuzu[@]}
    #do
       start=$(date +%s.%N) 
       for((j=1;j<=${ex_timer};j++));do
          {
           #echo "Test.test$i:1000|ms|@0.1|$i" | nc -u -w0 119.29.64.58 8125
           echo "${test}.test$j:1000|ms|@0.1|10000" | nc -u -w0 10.104.40.85 8126  
          }&
       done
       wait
       end=$(date +%s.%N)
       getTiming $start $end        
       sleep ${sleeper}
      
done

