#!/usr/bin/env python
#-*-coding:utf-8 -*-

#client端摸拟表单上传
import  urllib2
from  poster.encode import  multipart_encode
from  poster.streaminghttp import register_openers
import  sys
import  os


register_openers()



def upload_file(parameter_path,parameter_app):
    url = 'http://10.104.68.30:10000/upload/'
    os.chdir(parameter_path)
    datagen,headers = multipart_encode({"uploadfile":open(parameter_app,'rb')})
    request = urllib2.Request(url,datagen,headers)
    print  urllib2.urlopen(request).read()


if __name__ == '__main__':
    #包路径
    parameter_path = sys.argv[1]
    #环境_应用_版本_.tar.gz
    parameter_app = sys.argv[2]
    upload_file(parameter_path,parameter_app)
