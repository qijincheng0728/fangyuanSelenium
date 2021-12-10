'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/10 10:52
# @Author  : qijincheng
# @email   : 877767216@qq.com
# @Site    : 
# @File    : workAssistantTest.py
# @Software: PyCharm

'''
import unittest
from time import sleep
from common.login import login
from common.log import logger
from PO.workAssistantPage import Work_Assistant_Page
from common.myTest import MyTest

class WorkAssistantTest(MyTest):
    def test_click_WorkAssistant(self):

        wa = Work_Assistant_Page(self.driver)

        wa.click_WorkAssistant()
        logger.info('点击工作助理 完成')
        self.driver.implicitly_wait(10)

        wa.click_WorkAssistant_UserDataAuditAgent()
        logger.info('点击用户资料审核待办')
        self.driver.implicitly_wait(10)
        self.assertIn('资料审核代办列表',self.driver.page_source,'操作失败，请检查')
        sleep(2)

        wa.click_WorkAssistant_ListingReviewToDo()
        logger.info('点击房源审核待办工作')
        self.driver.implicitly_wait(10)
        self.assertIn('房源待办工作',self.driver.page_source,'操作失败，请检查')
        sleep(2)

        wa.click_WorkAssistant_RealHousePriceCustomerInformationManagement()
        logger.info('点击真实房价客户信息管理')
        self.driver.implicitly_wait(10)
        self.assertIn('真实房价客户信息管理', self.driver.page_source, '操作失败，请检查')
        sleep(2)

        wa.click_WorkAssistant_SimpleStoreAuditList()
        logger.info('点击简易版店铺审核列表')
        self.driver.implicitly_wait(10)
        self.assertIn('简易版店铺审核列表', self.driver.page_source, '操作失败，请检查')
        sleep(2)

        wa.click_WorkAssistant_ListingPreservationToDo()
        logger.info('点击房源保存待办工作')
        self.driver.implicitly_wait(10)
        self.assertIn('房源待办工作', self.driver.page_source, '操作失败，请检查')
        sleep(2)

        wa.click_WorkAssistant_RealNameCertificationToDo()
        logger.info('点击实名认证待办工作')
        self.driver.implicitly_wait(10)
        self.assertIn('实名认证待办工作', self.driver.page_source, '操作失败，请检查')
        sleep(2)

        wa.click_WorkAssistant_RegisterToDo()
        logger.info('点击注册待办工作')
        self.driver.implicitly_wait(10)
        self.assertIn('注册待办工作',self.driver.page_source,'操作失败，请检查')
        sleep(2)

        wa.click_WorkAssistant_CollectionOfHouseSourcePhotosAndReview()
        logger.info('点击采集房源照片审核')
        self.driver.implicitly_wait(10)
        self.assertIn('采集-照片墙', self.driver.page_source, '操作失败，请检查')
        sleep(2)

        wa.click_WorkAssistant_PendingReviewOfSuspectedIntermediaryListings()
        logger.info('点击疑似中介房源审核待办')
        self.driver.implicitly_wait(10)
        self.assertIn('疑似中介房源审核待办工作', self.driver.page_source, '操作失败，请检查')
        sleep(2)

        wa.click_WorkAssistant_StorageOfSuspectedIntermediaryHousesToDo()
        logger.info('点击疑似中介房源保存待办')
        self.driver.implicitly_wait(10)
        self.assertIn('疑似中介房源保存待办工作', self.driver.page_source, '操作失败，请检查')
        sleep(2)

if __name__ == '__main__':
    unittest.main(verbosity=2)