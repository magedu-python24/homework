# 本程序所使用的语言版本为:Python3.7
# -*-encoding: utf-8 -*-
# @Author    : Luo Guifeng
# @Email     : luoguifeng14@126.com
# @IDE       : PyCharm
# @Project   : homework
# @File      : Question _4.py
# @Date      : 2019/8/19
# @Time      : 12:26

my_list =[3, 5, 1, 7, 9, 6, 8]

print('排序前：', my_list)

for i in range(len(my_list)):
    min_index = i
    for j in range(i+1, len(my_list)):
        if my_list[min_index] > my_list[j]:
            min_index = j

    my_list[i], my_list[min_index] = my_list[min_index], my_list[i]

print('排序后：', my_list)
