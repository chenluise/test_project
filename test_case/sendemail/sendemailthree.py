#coding=utf-8
'''发送邮件--HTML文档内容加载到正文中'''
import smtplib
from email.mime.text import MIMEText
import time

sender = '215233848@qq.com'
receiver = 'chenlu11011@sina.com'
subject = 'python email test'
smtpserver = 'smtp.qq.com'
username = '215233848@qq.com'
password = 'uoyygabukibrbjcd'

file_new ='/Users/chenlu/Documents/bookmarks_2016_9_5.html'
f = open(file_new,'rb')
mail_body = f.read()
f.close()
msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
msg['subject']=u'自动化测试报告'
msg['date']=time.strftime("%Y-%m-%d %H.%M.%S")
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()

