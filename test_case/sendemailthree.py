#coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import unittest
import HTMLTestRunner
import time,os
from test_case.case import test_baidu
from test_case.case import test_youdao

#---------生成测试用例，套件/遍历----------

# def creatsuite():
#     suite = unittest.TestSuite()
#     tests = [test_youdao.YoudaoTest('test_youdao'),test_baidu.BaiduTest('test_baidu')]
#     suite.addTests(tests)


def creatsuite():
    test_dir = './case'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
    suite = unittest.TestSuite()
    suite.addTest(discover)
    return suite


#-----取出最新生成的报告----------
def send_reports():
    result_dir= 'F:\photo'
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn:os.path.getmtime(result_dir+"\\"+fn))
    print (u'最新测试生成的报告：'+lists[-1])
    file_new = os.path.join(result_dir,lists[-1])
    print file_new

    send_mails(file_new)

#----------发邮件----------------
def send_mails(file_new):
    sender = '215233848@qq.com'
    receiver = 'chenlu11011@sina.com'
    subject = 'python email test'
    smtpserver = 'smtp.qq.com'
    username = '215233848@qq.com'
    password = 'uoyygabukibrbjcd'
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()
    msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg['subject']=u'自动化测试报告'
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
    print (u'邮件已发出')


#--------将日志加上时间戳保存到路径文件-----------
if __name__ == '__main__':
    alltestnames=creatsuite()
    now = time.strftime("%Y-%m-%d %H.%M.%S")
    filename = 'F:\photo\oresult'+now+'.html'
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'百度搜索测试报告',
        description=u'用例执行情况：')


#--------按指定时间自动运行---------

    k=1
    while k<2:
        now_time = time.strftime('%H.%M')
        if now_time =='17.54':
            print (u'开始运行脚本')
            # runner = unittest.TextTestRunner
            runner.run(alltestnames)
            fp.close()
            send_reports()
            print (u'运行完成退出')
            break
        else:
            time.sleep(5)
            print (now_time)
