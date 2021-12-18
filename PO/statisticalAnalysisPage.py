'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/18 9:31
# @Author  : qijincheng
# @email   : 877767216@qq.com
# @Site    : 
# @File    : statisticalAnalysisPage.py
# @Software: PyCharm

'''
import time

from selenium.webdriver.common.by import By

from PO.basePage import BasePage

class StatisticalAnalysis(BasePage):
    StatisticalAnalysisPage = (By.XPATH,'/html/body/div[1]/div[1]/div[3]/ul/li[10]/a/p') # 统计分析主菜单按钮
    StatisticalAnalysisPage_MenuClickStatistics = (By.LINK_TEXT, '菜单点击统计')
    StatisticalAnalysisPage_StatisticalTableOfFeedbackInformation = (By.LINK_TEXT, '反馈信息统计表')
    StatisticalAnalysisPage_ActiveUserStatistics = (By.LINK_TEXT, '活跃用户数据统计')
    StatisticalAnalysisPage_AccountRevenueStatistics = (By.LINK_TEXT, '账号收益统计表')
    StatisticalAnalysisPage_SecondHandHousingSourceInformationStatistics = (By.LINK_TEXT, '二手房房源信息统计')
    StatisticalAnalysisPage_AccountStatisticsList = (By.LINK_TEXT, '账户统计列表')
    StatisticalAnalysisPage_OrderStatisticsList = (By.LINK_TEXT, '订单统计列表')
    StatisticalAnalysisPage_RewardTransactionStatistics = (By.LINK_TEXT, '悬赏交易统计表')
    StatisticalAnalysisPage_WorkAppraisalStatisticsForm = (By.LINK_TEXT, '工作考核统计表')
    StatisticalAnalysisPage_DetailedStatisticsOfPotentialCustomers = (By.LINK_TEXT, '潜在客户明细统计')
    StatisticalAnalysisPage_TotalStatisticsOfPotentialCustomers = (By.LINK_TEXT, '潜在客户合计统计表')
    StatisticalAnalysisPage_SmartRecommendationStatistics = (By.LINK_TEXT,'智能推荐统计表')
    StatisticalAnalysisPage_TelephoneCallsAndFeedbackStatistics = (By.LINK_TEXT, '电话拨打及反馈统计')
    StatisticalAnalysisPage_AccountStatistics_XPATH ='//*[@id="136"]/ul/li[1]/a' #账户统计表

    def click_StatisticalAnalysisPage(self):
        self.by_find_element(self.StatisticalAnalysisPage).click()
    def click_StatisticalAnalysisPage_MenuClickStatistics(self): #菜单点击统计
        target = self.driver.find_element_by_xpath(self.StatisticalAnalysisPage_AccountStatistics_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 显示在顶部
        self.by_find_element(self.StatisticalAnalysisPage_MenuClickStatistics).click()
    def click_StatisticalAnalysisPage_StatisticalTableOfFeedbackInformation(self): #反馈信息统计表
        target = self.driver.find_element_by_xpath(self.StatisticalAnalysisPage_AccountStatistics_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 显示在顶部
        self.by_find_element(self.StatisticalAnalysisPage_StatisticalTableOfFeedbackInformation).click()
    def click_StatisticalAnalysisPage_ActiveUserStatistics(self):  # 活跃用户数据统计
        target = self.driver.find_element_by_xpath(self.StatisticalAnalysisPage_AccountStatistics_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 显示在顶部
        self.by_find_element(self.StatisticalAnalysisPage_ActiveUserStatistics).click()
    def click_StatisticalAnalysisPage_AccountRevenueStatistics(self):  # 账号收益统计表
        target = self.driver.find_element_by_xpath(self.StatisticalAnalysisPage_AccountStatistics_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 显示在顶部
        self.by_find_element(self.StatisticalAnalysisPage_AccountRevenueStatistics).click()
    def click_StatisticalAnalysisPage_SecondHandHousingSourceInformationStatistics(self):  # 二手房房源信息统计
        target = self.driver.find_element_by_xpath(self.StatisticalAnalysisPage_AccountStatistics_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 显示在顶部
        self.by_find_element(self.StatisticalAnalysisPage_SecondHandHousingSourceInformationStatistics).click()
    def click_StatisticalAnalysisPage_AccountStatisticsList(self):  # 账户统计列表
        target = self.driver.find_element_by_xpath(self.StatisticalAnalysisPage_AccountStatistics_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 显示在顶部
        self.by_find_element(self.StatisticalAnalysisPage_AccountStatisticsList).click()
    def click_StatisticalAnalysisPage_OrderStatisticsList(self):  # 订单统计列表
        target = self.driver.find_element_by_xpath(self.StatisticalAnalysisPage_AccountStatistics_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 显示在顶部
        self.by_find_element(self.StatisticalAnalysisPage_OrderStatisticsList).click()
    def click_StatisticalAnalysisPage_RewardTransactionStatistics(self):  # 悬赏交易统计表
        target = self.driver.find_element_by_xpath(self.StatisticalAnalysisPage_AccountStatistics_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 显示在顶部
        self.by_find_element(self.StatisticalAnalysisPage_RewardTransactionStatistics).click()
    def click_StatisticalAnalysisPage_WorkAppraisalStatisticsForm(self):  # 工作考核统计表
        target = self.driver.find_element_by_xpath(self.StatisticalAnalysisPage_AccountStatistics_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 显示在顶部
        self.by_find_element(self.StatisticalAnalysisPage_WorkAppraisalStatisticsForm).click()
    def click_StatisticalAnalysisPage_DetailedStatisticsOfPotentialCustomers(self):  # 潜在客户明细统计
        target = self.driver.find_element_by_xpath(self.StatisticalAnalysisPage_AccountStatistics_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 显示在顶部
        self.by_find_element(self.StatisticalAnalysisPage_DetailedStatisticsOfPotentialCustomers).click()
    def click_StatisticalAnalysisPage_TotalStatisticsOfPotentialCustomers(self):  # 潜在客户合计统计表
        target = self.driver.find_element_by_xpath(self.StatisticalAnalysisPage_AccountStatistics_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 显示在顶部
        self.by_find_element(self.StatisticalAnalysisPage_TotalStatisticsOfPotentialCustomers).click()
    def click_StatisticalAnalysisPage_SmartRecommendationStatistics(self): #智能推荐统计表
        target = self.driver.find_element_by_xpath(self.StatisticalAnalysisPage_AccountStatistics_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 显示在顶部
        self.by_find_element(self.StatisticalAnalysisPage_SmartRecommendationStatistics).click()
    def click_StatisticalAnalysisPage_TelephoneCallsAndFeedbackStatistics(self):  # 电话拨打及反馈统计
        target = self.driver.find_element_by_xpath(self.StatisticalAnalysisPage_AccountStatistics_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 显示在顶部
        self.by_find_element(self.StatisticalAnalysisPage_TelephoneCallsAndFeedbackStatistics).click()

if __name__ == '__main__':
    from common.login import login
    driver = login().login()
    sa = StatisticalAnalysis(driver)
    sa.click_StatisticalAnalysisPage()
    sa.click_StatisticalAnalysisPage_SmartRecommendationStatistics()


