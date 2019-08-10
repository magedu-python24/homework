# 本程序所使用的语言为Python,版本号为3.7
# _*_encoding: utf-8 _*_
# @Author    : Luo Guifeng
# @Email     : luoguifeng14@126.com
# @Project   : homework
# @File      : homework
# @Date      : 2019/8/6
# @Time      : 13:14
# @IDE       : PyCharm2018.3

while True:
    print("请输入一个数字：")
    number1 = int(input())
    print("请输入操作符（+ - * /）：")
    operator = input()
    print("请输入另一个数字：")
    number2 = int(input())
    if operator == '+':
        print("result={}".format(number1 + number2))
    elif operator == '-':
        print("result={}".format(number1 - number2))
    elif operator == '*':
        print("result={}".format(number1 * number2))
    elif operator == '/':
        print("result={}".format(number1 / number2))
    else:
        print('输入有错误，请重新输入！！！')




