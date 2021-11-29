'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 16:44
# @Author  : qijincheng
# @email   : 877767216@qq.com
# @Site    : 
# @File    : login.py
# @Software: PyCharm

'''

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

from common.log import logger
from common.readConfig import ReadConfig



class login():
    def __init__(self):
        rc = ReadConfig()
        self.url = rc.readData('DATA','url')
        self.username = rc.readData('DATA','username')
        self.password = rc.readData('DATA', 'password')
    def login(self):
        url = self.url
        driver = webdriver.Chrome()
        driver.get(url=url)
        driver.maximize_window()
        # driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/div/form/div/div[2]/div[1]/div/input').send_keys('admin')
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/form/div/div[2]/div[1]/div/input').send_keys(self.username)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/div/form/div/div[2]/div[2]/div/input').send_keys(self.password)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/div/form/div/div[3]/button').click()
        logger.info('登陆成功。。。')

        # driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/ul/li[7]').click()
        # driver.find_element_by_xpath('/html/body/div[2]').click() # 从菜单切换到右面内容需要
        # driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr[1]/td[15]/div/a[1]').click()

        driver.implicitly_wait(10)
        return driver


if __name__=='__main__':
    login().login()





