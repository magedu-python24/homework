# 本程序所使用的语言版本为:Python3.7
# -*-encoding: utf-8 -*-
# @Author    : Luo Guifeng
# @Email     : luoguifeng14@126.com
# @IDE       : PyCharm
# @Project   : homework
# @File      : Question_5.py.py
# @Date      : 2019/8/20
# @Time      : 17:24
logs = '''
　
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200
　
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200
　
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200
　
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200
　
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200
　
'''

PostNum = 0
GetNum = 0
split_logs = logs.split('\n')

for i in split_logs:

    if len(i) < 1:
       split_logs.remove(i)

for i in split_logs:
    if len(i) == 1:
        split_logs.remove(i)

for str in split_logs:
    lower_logs = str.lower()
    split_str = lower_logs.split('"')
    operation_str = split_str[1]
    get_operation_str = operation_str.split()
    if 'post' in get_operation_str[0]:
        PostNum += 1

    else:
        GetNum += 1

print('PostNum {}'.format(PostNum), '\n', 'GetNum {}'.format(GetNum))