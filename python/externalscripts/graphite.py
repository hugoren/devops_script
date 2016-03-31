#!/usr/bin/env python
#-*-coding:utf-8-*-

import  urllib2 ,json,sys

def get_graphite(parameter):
    if len(sys.argv) == 1:
        print "please input parameter"
    else:
        parameter = sys.argv[1]
        url_parameter=parameter
        url='http://ip:8000/render/?&target=%s&from=-30s&format=json&integral'%url_parameter
        response=urllib2.urlopen(url)
        jrsp=json.loads(response.read())
        sum_jrsp = 0
        n = 0
        try:
            for i in jrsp[0]:
                if i == "datapoints":
                    for j in jrsp[0]['datapoints']:
                        if j[0] != None:
                            # print j[0]
                            sum_jrsp += j[0]
                            n += 1
            avg_jrsp = sum_jrsp/n
            print float(avg_jrsp)

        except EOFError:
            print  'ERR'
            sys.exit()


get_graphite=get_graphite("parameter")

#医生连接数
# doctor_connect=get_graphite("sumSeries(stats.timers.mobile.mobile{1,2,3,4}.gauge.ws-connect-count-doctor.mean)")
#
# #mobile微信公众号调用时间
# weixing_custom=get_graphite("averageSeries(stats.timers.mobile.mobile{1,2,3,4}.trace.Third-Weixin-custom-send.elapsed-time.mean)")
#
# #云通信调用时间
# ytx=get_graphite("averageSeries(stats.timers.mobile.mobile{1,2,3,4}.trace.Third-ytx-sendTemplateSMS.elapsed-time.mean)")
#
# #云之信调用时间
# ucpass=get_graphite("averageSeries(stats.timers.mobile.mobile{1,2,3,4}.trace.Third-Ucpaas-sendTemplateSMS.elapsed-time.mean)")
#
# #腾讯万象调用时间
# ppic_cloud=get_graphite("averageSeries(stats.timers.mobile.mobile{1,2,3,4}.trace.Third-picCloud-upload.elapsed-time.mean)")

# #cos调用时间
# file_cloud=get_graphite("averageSeries(stats.timers.mobile.mobile{1,2,3,4}.trace.Third-fileCloud-upload.elapsed-time.mean)")
#






