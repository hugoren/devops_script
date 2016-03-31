#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#export LANG=zh_CN.UTF-8 
import smtplib
from email.mime.text import MIMEText
import sys 
import chardet


reload(sys)
sys.setdefaultencoding('utf-8')


mail_host = "smtp.exmail.qq.com"    
mail_user = "xx@qq.com"
mail_pass = "**" 

mail_to = sys.argv[1]
subject = sys.argv[2]
#subject = subject.encode("utf-8")
content = sys.argv[3] + chardet.detect(subject)['encoding']



def send_mail(mail_user, mail_to, sub, content):
    msg = MIMEText(content, _subtype='plain')
    msg['Subject'] = sub
    msg['From'] = mail_user
    msg['To'] = mail_to
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)            
        s.login(mail_user, mail_pass)    
        s.sendmail(mail_user, mail_to, msg.as_string())  
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    with open('/tmp/message_zabbix','w') as f:
        f.writelines(chardet.detect(subject)['encoding'])
        f.writelines(content)
    send_mail(mail_user, mail_to, subject.decode( "ascii").encode("utf-8"), content.decode( "ascii").encode("utf-8"))
