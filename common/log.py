'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/24 14:07
# @Author  : qijincheng
# @email   : 877767216@qq.com
# @Site    : 
# @File    : log.py
# @Software: PyCharm

'''

import logging

def log():
    logging.basicConfig(
        level=logging.INFO, format = '%(name)s-%(asctime)s-级别:%(levelname)s-模块%(module)s.py-行号%(lineno)d-日志内容:%(message)s'
    )
    logger = logging.getLogger('appiumUI')
    return logger
logger = log()
if __name__ == '__main__':
    logger.info('这是我的自定义的日志')