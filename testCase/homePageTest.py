'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/24 15:09
# @Author  : qijincheng
# @email   : 877767216@qq.com
# @Site    : 
# @File    : homePageTest.py
# @Software: PyCharm

'''
import time
import unittest

from common.log import logger
from common.myTest import MyTest
from PO.homePage import HomePage
from common.login import login

class HomePageTest(MyTest):

    def test_click_homepage(self):
        hp = HomePage(self.driver)
        hp.click_firstpage()
        logger.info('点击首页 完成')
        self.driver.implicitly_wait(10)
        self.assertIn('发布房源',self.driver.page_source,'操作失败，请检查')

    # def test_click_WorkAssistant_UserDataAuditAgent(self):
    #     hp = HomePage(self.driver)
    #     hp.click_WorkAssistant()
    #     logger.info('点击工作助理 完成')
    #     self.driver.implicitly_wait(10)
    #     hp.click_WorkAssistant_UserDataAuditAgent()
    #     logger.info('点击用户资料审核待办')
    #     self.driver.implicitly_wait(10)
    #     self.assertIn('资料审核代办列表',self.driver.page_source,'操作失败，请检查')


if __name__ == '__main__':
    unittest.main(verbosity=2)11

