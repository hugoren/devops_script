# _*_ coding:utf-8 _*_
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import sys,os
# import chardet




mail_host = "smtp.exmail.qq.com"
mail_user = ""
mail_pass = ""

module_dir = os.path.dirname(__file__)
ip_path = os.path.join(module_dir,'ip.txt')
ip_home_path = os.path.join(module_dir,'ip_home.txt')
ip_content = open(ip_path)
ip_home_content = open(ip_home_path)


#mail_to = sys.argv[1]
#subject = sys.argv[1]
#content = sys.argv[3]
content_ip = ip_content.read()
content_ip_home = ip_home_content.read()
ip_content.close()
ip_home_content.close()

def send_mail(mail_user, mail_to, sub):

    # msg = MIMEText(content, _subtype='plain')
    msg = MIMEMultipart()
    msg['Subject'] = sub
    msg['From'] = mail_user
    msg['To'] = mail_to
    msg.attach(MIMEText("每天访问前100名ip统计:"))
    msg.attach(MIMEText(content_ip))
    msg.attach(MIMEText("每天访问/home主页前100名ip统计:"))
    msg.attach(MIMEText(content_ip_home))
    att_ip = MIMEApplication(open('ip.txt', 'rb').read())
    att_ip_home = MIMEApplication(open('ip_home.txt', 'rb').read())
    att_ip.add_header('Content-Disposition', 'attachment', filename="ip.txt")
    att_ip_home.add_header('Content-Disposition', 'attachment', filename="ip_home.txt")
    # att["Content-Type"] = 'application/octet-stream'
    att_ip["Content-Disposition"] = 'download'
    msg.attach(att_ip)
    msg.attach(att_ip_home)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user, mail_pass)
        s.sendmail(mail_user, mail_to, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print e.message
        return False
if __name__ == '__main__':
    mail_user_list = ["a","b","c"]
    for u in mail_user_list:
        send_mail(mail_user, u, "每天的路径/与/home访问数统计前100个")
