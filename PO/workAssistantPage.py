'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/10 10:40
# @Author  : qijincheng
# @email   : 877767216@qq.com
# @Site    : 
# @File    : workAssistantPage.py
# @Software: PyCharm

'''
from selenium.webdriver.common.by import By
from PO.basePage import BasePage


class Work_Assistant_Page(BasePage):
    WorkAssistant = (By.XPATH, '/html/body/div[1]/div[1]/div[3]/ul/li[2]/a/p') #工作助理主菜单按钮
    WorkAssistant_UserDataAuditAgent = (By.LINK_TEXT, "用户资料审核代办工作") #工作助理-用户资料审核代办工作按钮
    WorkAssistant_ListingReviewToDo = (By.LINK_TEXT,'房源审核待办工作') #工作助理-房源审核待办工作按钮
    WorkAssistant_RealHousePriceCustomerInformationManagement = (By.LINK_TEXT,'真实房价客户信息管理') #工作助理-真实房价客户信息管理按钮
    WorkAssistant_SimpleStoreAuditList = (By.LINK_TEXT,'简易版店铺审核列表') #工作助理-简易版店铺审核列表按钮
    WorkAssistant_ListingPreservationToDo = (By.LINK_TEXT,'房源保存待办工作') #工作助理-房源保存待办工作按钮
    WorkAssistant_RealNameCertificationToDo = (By.LINK_TEXT,'实名认证待办工作') #工作助理-实名认证待办工作按钮
    WorkAssistant_RegisterToDo = (By.LINK_TEXT,'注册待办工作') #工作助理-注册待办工作按钮
    WorkAssistant_CollectionOfHouseSourcePhotosAndReview = (By.LINK_TEXT,'采集房源照片审核') #工作助理-采集房源照片审核按钮
    WorkAssistant_PendingReviewOfSuspectedIntermediaryListings = (By.LINK_TEXT,'疑似中介房源审核待办') #工作助理-疑似中介房源审核待办按钮
    WorkAssistant_StorageOfSuspectedIntermediaryHousesToDo = (By.LINK_TEXT,'疑似中介房源保存待办') #工作助理-疑似中介房源保存待办按钮



    def click_WorkAssistant(self): #点击工作助理主菜单按钮
        self.by_find_element(self.WorkAssistant).click()

    def click_WorkAssistant_UserDataAuditAgent(self): #点击工作助理-用户资料审核代办工作按钮
        self.by_find_element(self.WorkAssistant_UserDataAuditAgent).click()

    def click_WorkAssistant_ListingReviewToDo(self): #点击工作助理-房源审核待办工作按钮
        self.by_find_element(self.WorkAssistant_ListingReviewToDo).click()

    def click_WorkAssistant_RealHousePriceCustomerInformationManagement(self): #点击工作助理-真实房价客户信息管理按钮
        self.by_find_element(self.WorkAssistant_RealHousePriceCustomerInformationManagement).click()

    def click_WorkAssistant_SimpleStoreAuditList(self): #点击工作助理-简易版店铺审核列表按钮
        self.by_find_element(self.WorkAssistant_SimpleStoreAuditList).click()

    def click_WorkAssistant_ListingPreservationToDo(self): #点击工作助理-房源保存待办工作按钮
        self.by_find_element(self.WorkAssistant_ListingPreservationToDo).click()

    def click_WorkAssistant_RealNameCertificationToDo(self): #点击工作助理-实名认证待办工作按钮
        self.by_find_element(self.WorkAssistant_RealNameCertificationToDo).click()

    def click_WorkAssistant_RegisterToDo(self): #点击工作助理-注册待办工作按钮
        self.by_find_element(self.WorkAssistant_RegisterToDo).click()

    def click_WorkAssistant_CollectionOfHouseSourcePhotosAndReview(self): #点击工作助理-采集房源照片审核按钮
        self.by_find_element(self.WorkAssistant_CollectionOfHouseSourcePhotosAndReview).click()

    def click_WorkAssistant_PendingReviewOfSuspectedIntermediaryListings(self): #点击工作助理-疑似中介房源审核待办按钮
        self.by_find_element(self.WorkAssistant_PendingReviewOfSuspectedIntermediaryListings).click()

    def click_WorkAssistant_StorageOfSuspectedIntermediaryHousesToDo(self): #点击工作助理-疑似中介房源保存待办按钮
        self.by_find_element(self.WorkAssistant_StorageOfSuspectedIntermediaryHousesToDo).click()