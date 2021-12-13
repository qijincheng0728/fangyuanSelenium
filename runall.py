'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/11 10:40
# @Author  : qijincheng
# @email   : 877767216@qq.com
# @Site    : 
# @File    : runall.py
# @Software: PyCharm

'''

import os,time,unittest

from common.HTMLTestRunner_old import HTMLTestReportCN

dirName = os.path.dirname(__file__)
def creat_suit():
    filedir = dirName+'/testCase/'
    suite = unittest.defaultTestLoader.discover(start_dir=filedir,pattern='*Test.py')
    return suite
if __name__ == '__main__':
    cur_time = time.strftime('%Y%m%d%H%M%S',time.localtime())
    fimename = dirName+'/Report/report'+cur_time+'.html'
    with open(fimename,'wb') as f:
        runner = HTMLTestReportCN(stream=f,title='房源管理后台冒烟测试报告',description='报告描述',tester='齐津铖')
        runner.run(creat_suit())