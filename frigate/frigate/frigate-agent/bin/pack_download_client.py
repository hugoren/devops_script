#!/usr/bin/env python
#coding:utf-8
import  requests
import  sys
import  os



def download_file(download_dir,parameter_app):
    url = 'http://10.104.68.30:10000/download_client/%s'%parameter_app
    r = requests.get(url)
    os.chdir(download_dir)
    try:
        with open("%s"%parameter_app,"wb") as pack_content:
            pack_content.write(r.content)
        print "下载成功!"
    except Exception as e:
        return e.message

if __name__ == '__main__':
    #存储路径
    download_dir = sys.argv[1]
    #下载包名称
    parameter_app = sys.argv[2]
    download_file(download_dir,parameter_app)




