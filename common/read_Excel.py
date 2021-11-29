'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/14 9:20
# @Author  : qijincheng
# @email   : 877767216@qq.com
# @Site    : 
# @File    : read_Excel.py
# @Software: PyCharm

'''

import xlrd,os
class readexcel():
    dir = 'testdata'
    excel_dir = os.path.dirname(os.getcwd()) + '\\' + dir
    # excel_dir = os.getcwd() +'\\'+dir
    # print(excel_dir)
    workbook = xlrd.open_workbook(excel_dir + '\\' + 'jiekoudata.xls')
    sheet1 = workbook.sheet_by_index(0)
    urlSheet =workbook.sheet_by_name('urlSheet')
    paramSheet = workbook.sheet_by_name('paramSheet')
    assertSheet = workbook.sheet_by_name('assertSheet')

    urlrownum = urlSheet.nrows
    paramrownum = paramSheet.nrows
    assertrownum = paramSheet.nrows
    # print(rownum)

    def readexcel(self):
        urllist = []
        # 获取url列表
        # print(self.rownum)
        for i in range(1, self.urlrownum):
            # 获取urlsheet里面的值
            self.rowvalue = self.urlSheet.row_values(i)
            # print(self.rowvalue)
            urllist.append(self.rowvalue)
        print(urllist)
        return urllist


if __name__ == '__mian__':
    readexcel().readexcel()