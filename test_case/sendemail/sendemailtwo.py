#coding=utf-8
'''发送邮件--（带附件）'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = '215233848@qq.com'
receiver = 'chenlu11011@sina.com'
subject = 'python email test'
smtpserver = 'smtp.qq.com'
username = '215233848@qq.com'
password = 'uoyygabukibrbjcd'

msgRoot = MIMEMultipart('related')
msgRoot['subject'] = subject

att = MIMEText(open('F:\photo\oresult2018-08-13 15.53.07.html','rb').read(),'base64','utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="test.html"'
msgRoot.attach(att)

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username,password)
smtp.sendmail(sender,receiver,msgRoot.as_string())
smtp.quit()

