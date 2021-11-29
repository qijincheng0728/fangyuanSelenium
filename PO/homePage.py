'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/24 14:00
# @Author  : qijincheng
# @email   : 877767216@qq.com
# @Site    : 
# @File    : homePage.py
# @Software: PyCharm

'''
import time

import time
from selenium.webdriver.common.by import By
from PO.basePage import BasePage
from common.log import logger
from common.login import login
from common.readConfig import ReadConfig

class HomePage(BasePage):
    firstpage = (By.XPATH, '/html/body/div[1]/div[1]/div[3]/ul/li[1]/a')

    WorkAssistant = (By.XPATH,'/html/body/div[1]/div[1]/div[3]/ul/li[2]/a/p')

    WorkAssistant_UserDataAuditAgent = (By.LINK_TEXT,"用户资料审核代办工作")

    def click_firstpage(self):
        self.by_find_element(self.firstpage).click()

    def click_WorkAssistant(self):
        self.by_find_element(self.WorkAssistant).click()

    def click_WorkAssistant_UserDataAuditAgent(self):
        self.by_find_element(self.WorkAssistant_UserDataAuditAgent).click()

if __name__ == '__main__':
    from common.login import login
    lg = login()
    driver = lg.login()
    hp = HomePage(driver)
    hp.click_firstpage()
    driver.implicitly_wait(10)
    hp.click_WorkAssistant()
    driver.implicitly_wait(10)
    hp.click_WorkAssistant_UserDataAuditAgent()






