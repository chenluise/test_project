#coding=utf-8
'''查找文件中最新的报告'''

import os

result_dir = 'F:\photo'
lists = os.listdir(result_dir)

lists.sort(key=lambda fn:os.path.getmtime(result_dir+"\\"+fn))

print ('最新的文件为：'+lists[-1])
file = os.path.join(result_dir,lists[-1])
print file











