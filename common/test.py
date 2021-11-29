'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/27 16:14
# @Author  : qijincheng
# @email   : 877767216@qq.com
# @Site    : 
# @File    : test.py
# @Software: PyCharm

'''

import random

# 提示：0-布，1-剪⼑，2-⽯头
com = random.randint(0,2)
p = int(input('请出拳：'))

if p == 0:
    print('玩家出布')
elif p == 1:
    print('玩家出剪刀')
elif p == 2:
    print('玩家出石头')
else:
    print('出拳错误')

if com == 0:
    print('电脑出布')
elif com == 1:
    print('电脑出剪刀')
else:
    print('电脑出石头')
if 0>p or p>2:
    print('玩家出拳错误，结束')
else:
    if com>=1 and p>com or p==1 and com==0 or p==0 and com==2:
        print('玩家胜利')
    elif p == com:
        print('平局')
    else:
        print('电脑胜利')

# if com>=1 and p>com:
#     print('玩家胜利')
# elif p==1 and com==0:
#     print('玩家胜利')
# elif p==0 and com==2:
#     print('玩家胜利')
# elif p==2 and com==0:
#     print('电脑胜利')
# elif p == com:
#     print('平局')
# else:
#     print('电脑胜利')
