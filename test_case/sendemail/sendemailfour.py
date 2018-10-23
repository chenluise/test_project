#coding=utf-8
'''查找最近的文件，发送邮件 （此处调用了sendemailALL里的发送函数）'''

import time
from email.mime.text import MIMEText
import os
import sendemailALL

result_dir ='/Users/chenlu/dev/testresult'
list = os.listdir(result_dir)
list.sort(key=lambda fn:os.path.getmtime(result_dir+'/'+fn))
file_one = os.path.join(result_dir,list[-1])

sendemailALL.send_mails(file_one)