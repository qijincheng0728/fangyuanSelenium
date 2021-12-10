'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/10 13:50
# @Author  : qijincheng
# @email   : 877767216@qq.com
# @Site    : 
# @File    : housingInformationManagementPage.py
# @Software: PyCharm

'''
from selenium.webdriver.common.by import By

from PO.basePage import BasePage
from time import sleep

class HousingInformationManagementPage(BasePage):
    HousingInformationManagement = (By.XPATH,'/html/body/div[1]/div[1]/div[3]/ul/li[4]/a/p') #房源信息管理主菜单按钮
    HousingInformationManagement_OfficialListingReviewFeedbackManagement = (By.LINK_TEXT,'官方房源审核反馈管理') #房源信息管理-官方房源审核反馈管理按钮
    HousingInformationManagement_RewardListingManagement = (By.LINK_TEXT,'悬赏房源管理')  #房源信息管理-悬赏房源管理按钮
    HousingInformationManagement_SecondHandHousingManagement = (By.LINK_TEXT,'二手房源管理') #房源信息管理-二手房源管理
    HousingInformationManagement_ListingsCollectionListingsTable = (By.LINK_TEXT, '房源-采集房源表') #房源信息管理-房源-采集房源表
    HousingInformationManagement_FollowUpUnansweredList = (By.LINK_TEXT,'回访无人接听列表') #房源信息管理-回访无人接听列表
    HousingInformationManagement_PotentialOwnerManagement = (By.LINK_TEXT, '潜在业主管理') #房源信息管理-潜在业主管理
    HousingInformationManagement_FirstHandInformation = (By.LINK_TEXT, '一手信息') #房源信息管理-一手信息
    HousingInformationManagement_HousingSourceRentalHousingCollectionForm = (By.LINK_TEXT, '房源-出租房采集表') #房源信息管理-房源-出租房采集表
    HousingInformationManagement_HousingSupplyFeedbackManagement = (By.LINK_TEXT, '房源反馈管理') #房源信息管理-房源反馈管理
    HousingInformationManagement_ListingInvitationManagement = (By.LINK_TEXT, '房源邀请管理') #房源信息管理-房源邀请管理
    HousingInformationManagement_TelephoneResourceManagement = (By.LINK_TEXT, '电话资源管理')  #房源信息管理-电话资源管理
    HousingInformationManagement_HousingRecyclingBin = (By.LINK_TEXT,'房源回收站') #房源信息管理-房源回收站
    HousingInformationManagement_ExclusiveSigningList = (By.LINK_TEXT, '签约独家列表')  # 房源信息管理-签约独家列表
    HousingInformationManagement_ListingInvitationManagement_XPath = '//*[@id="127"]/ul/li[10]/a'

    def click_HousingInformationManagement(self): #点击房源信息管理主菜单按钮
        self.by_find_element(self.HousingInformationManagement).click()

    def click_HousingInformationManagement_OfficialListingReviewFeedbackManagement(self): #点击房源信息管理-官方房源审核反馈管理按钮
        self.by_find_element(self.HousingInformationManagement_OfficialListingReviewFeedbackManagement).click()

    def click_HousingInformationManagement_RewardListingManagement(self): #点击房源信息管理-悬赏房源管理按钮
        self.by_find_element(self.HousingInformationManagement_RewardListingManagement).click()

    def click_HousingInformationManagement_SecondHandHousingManagement(self): #点击房源信息管理-二手房源管理按钮
        self.by_find_element(self.HousingInformationManagement_SecondHandHousingManagement).click()

    def click_HousingInformationManagement_ListingsCollectionListingsTable(self): #点击房源信息管理-房源-采集房源表按钮
        self.by_find_element(self.HousingInformationManagement_ListingsCollectionListingsTable).click()

    def click_HousingInformationManagement_FollowUpUnansweredList(self): #点击房源信息管理-回访无人接听列表按钮
        self.by_find_element(self.HousingInformationManagement_FollowUpUnansweredList).click()

    def click_HousingInformationManagement_PotentialOwnerManagement(self): #点击房源信息管理-潜在业主管理按钮
        self.by_find_element(self.HousingInformationManagement_PotentialOwnerManagement).click()

    def click_HousingInformationManagement_FirstHandInformation(self): #点击房源信息管理-一手信息按钮
        self.by_find_element(self.HousingInformationManagement_FirstHandInformation).click()

    def click_HousingInformationManagement_HousingSourceRentalHousingCollectionForm(self): #点击房源信息管理-房源-出租房采集表按钮
        self.by_find_element(self.HousingInformationManagement_HousingSourceRentalHousingCollectionForm).click()

    def click_HousingInformationManagement_HousingSupplyFeedbackManagement(self): #点击房源信息管理-房源反馈管理按钮
        self.by_find_element(self.HousingInformationManagement_HousingSupplyFeedbackManagement).click()

    def click_HousingInformationManagement_ListingInvitationManagement(self): #点击房源信息管理-房源邀请管理按钮
        target = self.driver.find_element_by_xpath(self.HousingInformationManagement_ListingInvitationManagement_XPath)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 显示在顶部
        # self.driver.execute_script("arguments[0].focus();", target)   #显示在中间
        self.by_find_element(self.HousingInformationManagement_ListingInvitationManagement).click()

    def click_HousingInformationManagement_TelephoneResourceManagement(self): #点击房源信息管理-电话资源管理按钮
        target = self.driver.find_element_by_xpath(self.HousingInformationManagement_ListingInvitationManagement_XPath)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 显示在顶部
        # self.driver.execute_script("arguments[0].focus();", target)   #显示在中间
        self.by_find_element(self.HousingInformationManagement_TelephoneResourceManagement).click()

    def click_HousingInformationManagement_HousingRecyclingBin(self): #点击房源信息管理-房源回收站按钮
        target = self.driver.find_element_by_xpath(self.HousingInformationManagement_ListingInvitationManagement_XPath)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 显示在顶部
        # self.driver.execute_script("arguments[0].focus();", target)   #显示在中间
        self.by_find_element(self.HousingInformationManagement_HousingRecyclingBin).click()

    def click_HousingInformationManagement_ExclusiveSigningList(self): # 点击房源信息管理-签约独家列表按钮
        target = self.driver.find_element_by_xpath(self.HousingInformationManagement_ListingInvitationManagement_XPath)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 显示在顶部
        # self.driver.execute_script("arguments[0].focus();", target)   #显示在中间
        self.by_find_element(self.HousingInformationManagement_ExclusiveSigningList).click()

    # def execute_script(self, param, aa):
    #     pass


if __name__ == '__main__':
    from common.login import login
    lg = login().login()
    him = HousingInformationManagementPage(lg)
    him.click_HousingInformationManagement()

