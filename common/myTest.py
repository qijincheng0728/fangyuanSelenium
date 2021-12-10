'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/24 15:09
# @Author  : qijincheng
# @email   : 877767216@qq.com
# @Site    : 
# @File    : myTest.py
# @Software: PyCharm

'''

import unittest
from common.login import login
from common.log import logger

class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

        logger.info('kai')
    def setUp(self):
        da = login()
        self.driver = da.login()
        logger.info('开1')
    def tearDown(self):
        self.driver.quit()
        logger.info('关1')
    @classmethod
    def tearDownClass(cls):
        pass
        logger.info('guan')

# class MyTest(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         dr = login()
#         cls.driver = dr.login()
#     def setUp(self):
#         da = login()
#         self.driver = da.login()
#         logger.info('开1')
#     def tearDown(self):
#         self.driver.quit()
#         logger.info('关1')
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
#         logger.info('关')

if __name__ == '__main__':
    unittest.main(verbosity=2)

