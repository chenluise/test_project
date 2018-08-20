#coding=utf-8
'''发送邮件--（文本）'''

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '215233848@qq.com'
receiver = 'chenlu11011@sina.com'
subject = 'python email test'
smtpserver = 'smtp.qq.com'
username = '215233848@qq.com'
password = 'uoyygabukibrbjcd'

msg = MIMEText('<html><h1>测试邮件！</h1></html>','html','utf-8')
msg['subject'] = Header(subject,'utf-8')

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()

