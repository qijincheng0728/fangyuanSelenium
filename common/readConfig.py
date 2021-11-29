'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/24 14:18
# @Author  : qijincheng
# @email   : 877767216@qq.com
# @Site    : 
# @File    : readConfig.py
# @Software: PyCharm

'''

import configparser,os
from common.log import logger

class ReadConfig():
    def __init__(self):
        self.file = os.path.dirname(os.path.dirname(__file__))+'/config.ini' #获取config.ini的位置
        self.conf = configparser.ConfigParser()
        self.conf.read(self.file,encoding='utf-8')
        logger.info('driver数据读取完毕')
    def readData(self,section,option = 'all'):
        try:
            if option == 'all':
                return self.conf.items(section)
            else:
                return self.conf.get(section,option)
        except Exception as msg:
            logger.info('读取配置文件失败,系统提示:%s'%msg)

if __name__ == '__main__':
    rc = ReadConfig()
    logger.info(rc.readData('DATA'))
    logger.info(rc.readData('DATA','url'))