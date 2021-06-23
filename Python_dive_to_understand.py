#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Python_dive_to_understand.py
@Time    :   2021/06/19 11:19:02
@Author  :   Chenfeng Yuan 
@Address :   Shapingba district, Chongqing, China
@Version :   1.0
@Contact :   chenfengyuan@cqu.edu.cn
@License :   (C)Copyright 2021-2022, Chengroup-CQU-Structural-Wind-Engineering
@Desc    :   None
@Goal    :   针对PTA上面的Python编程题目深入理解Python基本的数据结构和语法。
'''

# here put the import lib

#%% 源程序-任意进制转十进制（此处任意进制仅限于十进制内，不含字母）
"""
"""
a, b = input().split(",")
n = len(a)
b, s = int(b), 0
for i in range(n):
    s += int(a[i])*(b**(n-1-i))
print(s)

#%% 
# x = input()
x = "12"
n = len(x)
print(x)
print(n)
print(x[0])
# %%
