'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/24 14:00
# @Author  : qijincheng
# @email   : 877767216@qq.com
# @Site    : 
# @File    : basePage.py
# @Software: PyCharm

'''
from selenium.webdriver.common.by import By

from common.log import logger

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self,driver):
        self.driver = driver
    def by_find_element(self,item):
        try:
            element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located(item))
            logger.info('找到元素了')
            return  element
        except Exception as msg:
            logger.info('系统提示的错误信息 %s'%msg)
    def by_find_elements(self,item):
        try:
            element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_all_elements_located(item))
            logger.info('找到元素了')
            return element
        except Exception as msg:
            logger.info('系统提示的错误信息 %s'%msg)

if __name__ == '__main__':
    from common.login import login
    lg = login()
    driver = lg.login()
    Bp = BasePage(driver)
    a = (By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/form/div/div[2]/div[1]/div/input')
    Bp.by_find_element(a)

