'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/10 13:58
# @Author  : qijincheng
# @email   : 877767216@qq.com
# @Site    : 
# @File    : housingInformationManagementTest.py
# @Software: PyCharm

'''

import unittest
from time import sleep

from selenium.webdriver.common.by import By

from common.myTest import MyTest
from common.log import logger
from PO.housingInformationManagementPage import HousingInformationManagementPage

from selenium.webdriver.common.action_chains import ActionChains


class HousingInformationManagementTest(MyTest):
    def test_cilck_HousingInformationManagement(self):
        him = HousingInformationManagementPage(self.driver)

        him.click_HousingInformationManagement()
        logger.info('点击房源信息管理主菜单按钮')
        self.driver.implicitly_wait(10)

        him.click_HousingInformationManagement_OfficialListingReviewFeedbackManagement()
        logger.info('点击房源信息管理-官方房源审核反馈管理按钮')
        self.driver.implicitly_wait(10)
        self.assertIn('中介名称',self.driver.page_source,'操作失败，请检查')
        sleep(2)

        him.click_HousingInformationManagement_RewardListingManagement()
        logger.info('点击房源信息管理-悬赏房源管理按钮')
        self.driver.implicitly_wait(10)
        self.assertIn('悬赏房源管理',self.driver.page_source,'操作失败，请检查')
        sleep(2)

        him.click_HousingInformationManagement_SecondHandHousingManagement()
        logger.info('点击房源信息管理-二手房源管理按钮')
        self.driver.implicitly_wait(10)
        self.assertIn('二手房源管理',self.driver.page_source,'操作失败，请检查')
        sleep(2)

        him.click_HousingInformationManagement_ListingsCollectionListingsTable()
        logger.info('点击房源信息管理-房源-采集房源表按钮')
        self.driver.implicitly_wait(10)
        self.assertIn('房源-采集房源表',self.driver.page_source,'操作失败，请检查')
        sleep(2)

        him.click_HousingInformationManagement_FollowUpUnansweredList()
        logger.info('点击房源信息管理-回访无人接听列表按钮')
        self.driver.implicitly_wait(10)
        self.assertIn('房源-回访无人接听列表',self.driver.page_source,'操作失败，请检查')
        sleep(2)

        him.click_HousingInformationManagement_PotentialOwnerManagement()
        logger.info('点击房源信息管理-潜在业主管理按钮')
        self.driver.implicitly_wait(10)
        self.assertIn('房源-潜在业主管理',self.driver.page_source,'操作失败，请检查')
        sleep(2)

        him.click_HousingInformationManagement_FirstHandInformation()
        logger.info('点击房源信息管理-一手信息按钮')
        self.driver.implicitly_wait(10)
        self.assertIn('二手房源管理',self.driver.page_source,'操作失败，请检查')
        sleep(2)

        him.click_HousingInformationManagement_HousingSourceRentalHousingCollectionForm()
        logger.info('点击房源信息管理-房源-出租房采集表按钮')
        self.driver.implicitly_wait(10)
        self.assertIn('来源地址',self.driver.page_source,'操作失败，请检查')
        sleep(2)

        him.click_HousingInformationManagement_HousingSupplyFeedbackManagement()
        logger.info('点击房源信息管理-房源反馈管理按钮')
        self.driver.implicitly_wait(10)
        self.assertIn('反馈时间',self.driver.page_source,'操作失败，请检查')
        sleep(2)

        him.click_HousingInformationManagement_ListingInvitationManagement()
        logger.info('点击房源信息管理-房源邀请管理按钮')
        self.driver.implicitly_wait(10)
        self.assertIn('会员房源邀请记录表',self.driver.page_source,'操作失败，请检查')
        sleep(2)

        him.click_HousingInformationManagement_TelephoneResourceManagement()
        logger.info('点击房源信息管理-电话资源管理按钮')
        self.driver.implicitly_wait(10)
        self.assertIn('电话资源管理', self.driver.page_source, '操作失败，请检查')
        sleep(2)

        him.click_HousingInformationManagement_HousingRecyclingBin()
        logger.info('点击房源信息管理-房源回收站按钮')
        self.driver.implicitly_wait(10)
        self.assertIn('房源-房源回收站', self.driver.page_source, '操作失败，请检查')
        sleep(2)

        him.click_HousingInformationManagement_ExclusiveSigningList()
        logger.info('点击房源信息管理-签约独家列表按钮')
        self.driver.implicitly_wait(10)
        self.assertIn('签约独家列表', self.driver.page_source, '操作失败，请检查')
        sleep(2)

if __name__ == '__main__':
    unittest.main(verbosity=2)


