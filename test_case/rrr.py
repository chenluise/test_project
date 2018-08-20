#coding=utf-8

'''整合选择最新的测试报告，使用框架，自动发邮件'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import unittest
import HTMLTestRunner
import time,os
from test_case.case import test_baidu
from test_case.case import test_youdao

#'''定义发送邮件'''
def send_mail(file_new):
    sender = '215233848@qq.com'
    receiver = 'chenlu11011@sina.com'
    smtpserver = 'smtp.qq.com'
    username = '215233848@qq.com'
    password = 'uoyygabukibrbjcd'
    subject = open(file_new,'rb')
    mail_body = subject.read()
    subject.close()
    msg=MIMEText(mail_body,_subtype='html',_charset=utf-8)

    msg['subject']=u'自动化测试报告'
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()
    print 'email has send out!'

#-----查找测试报告目录，找到最新生成的测试报告文件----
def send_report(testreport):
    result_dir=testreport
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn:os.path.getmtime(result_dir+"\\"+fn))
    print (u'最新测试生成的报告：'+lists[-1])
    file_new = os.path.join(result_dir,lists[-1])
    print file_new

    send_mail(file_new)

#---------将用例添加到测试套件----------
def creatsuite():

    test_dir = './case'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
    suite = unittest.TestSuite()
    suite.addTest(discover)
    return suite


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H.%M.%S")
    testreport='F:\photo'
    with open('F:\photo\oresult'+now+'.html','wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title=u"百度搜索测试报告",
            description=u"用例执行情况：",
            verbosity=2
        )
    alltestname=creatsuite()
    runner.run(alltestname)
    f.close()
    send_report(testreport)





