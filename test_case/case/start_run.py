#coding=utf-8
'''自动执行测试用例，到时间点开始执行'''
import os,time

k=1
while k<2:
    now_time = time.strftime('%H.%M')
    if now_time =='17.47':
        print u'开始运行脚本：'
        os.chdir(u"/Users/chenlu/软件/PyCharm/test_project/test_case/case")
        os.system('python html.py')
        print  u'执行完成退出'
        break
    else:
        time.sleep(10)
        print (now_time)
