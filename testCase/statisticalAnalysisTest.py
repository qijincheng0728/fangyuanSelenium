'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/18 13:32
# @Author  : qijincheng
# @email   : 877767216@qq.com
# @Site    : 
# @File    : statisticalAnalysisTest.py
# @Software: PyCharm

'''

from common.log import logger
from common.myTest import MyTest
from PO.statisticalAnalysisPage import StatisticalAnalysis
import unittest
from time import sleep

class StatisticalAnalysisTest(MyTest):
    def test_click_StatisticalAnalysis(self):
        sa = StatisticalAnalysis(self.driver)

        sa.click_StatisticalAnalysisPage()
        logger.info('点击统计分析主菜单按钮')
        self.driver.implicitly_wait(10)

        sa.click_StatisticalAnalysisPage_MenuClickStatistics() #菜单点击统计
        logger.info('点击菜单点击统计')
        self.driver.implicitly_wait(10)
        self.assertIn('菜单点击统计-列表',self.driver.page_source,'操作失败，请检查')
        sleep(2)

        sa.click_StatisticalAnalysisPage_StatisticalTableOfFeedbackInformation() #反馈信息统计表
        logger.info('点击反馈信息统计表')
        self.driver.implicitly_wait(10)
        self.assertIn('反馈信息统计表',self.driver.page_source,'操作失败，请检查')
        sleep(2)

        sa.click_StatisticalAnalysisPage_ActiveUserStatistics()
        logger.info('点击活跃用户数据统计')
        self.driver.implicitly_wait(10)
        self.assertIn('服务号活跃用户数据统计',self.driver.page_source,'操作失败，请检查')
        sleep(2)

        sa.click_StatisticalAnalysisPage_AccountRevenueStatistics()
        logger.info('点击账号收益统计表')
        self.driver.implicitly_wait(10)
        self.assertIn('账号收益统计表', self.driver.page_source, '操作失败，请检查')
        sleep(2)

        sa.click_StatisticalAnalysisPage_SecondHandHousingSourceInformationStatistics()
        logger.info('点击二手房房源信息统计')
        self.driver.implicitly_wait(10)
        self.assertIn('统计-二手房房源信息统计', self.driver.page_source, '操作失败，请检查')
        sleep(2)

        sa.click_StatisticalAnalysisPage_AccountStatisticsList()
        logger.info('点击账户统计列表')
        self.driver.implicitly_wait(10)
        self.assertIn('账户统计列表', self.driver.page_source, '操作失败，请检查')
        sleep(2)

        sa.click_StatisticalAnalysisPage_OrderStatisticsList()
        logger.info('点击订单统计列表')
        self.driver.implicitly_wait(10)
        self.assertIn('订单统计列表', self.driver.page_source, '操作失败，请检查')
        sleep(2)

        sa.click_StatisticalAnalysisPage_RewardTransactionStatistics()
        logger.info('点击悬赏交易统计表')
        self.driver.implicitly_wait(10)
        self.assertIn('悬赏房源管理', self.driver.page_source, '操作失败，请检查')
        sleep(2)

        sa.click_StatisticalAnalysisPage_WorkAppraisalStatisticsForm()
        logger.info('点击工作考核统计表')
        self.driver.implicitly_wait(10)
        self.assertIn('工作考核统计表', self.driver.page_source, '操作失败，请检查')
        sleep(2)

        sa.click_StatisticalAnalysisPage_DetailedStatisticsOfPotentialCustomers()
        logger.info('点击潜在客户明细统计')
        self.driver.implicitly_wait(10)
        self.assertIn('潜在客户统计', self.driver.page_source, '操作失败，请检查')
        sleep(2)

        sa.click_StatisticalAnalysisPage_TotalStatisticsOfPotentialCustomers()
        logger.info('点击潜在客户合计统计表')
        self.driver.implicitly_wait(10)
        self.assertIn('潜在客户合计统计表', self.driver.page_source, '操作失败，请检查')
        sleep(2)

        sa.click_StatisticalAnalysisPage_SmartRecommendationStatistics()
        logger.info('点击智能推荐统计表')
        self.driver.implicitly_wait(10)
        self.assertIn('智能推荐统计表', self.driver.page_source, '操作失败，请检查')
        sleep(2)

        sa.click_StatisticalAnalysisPage_TelephoneCallsAndFeedbackStatistics()
        logger.info('点击电话拨打及反馈统计')
        self.driver.implicitly_wait(10)
        self.assertIn('统计-电话拨打及反馈数据统计', self.driver.page_source, '操作失败，请检查')
        sleep(2)

if __name__ == '__main__':
    unittest.main(verbosity=2)