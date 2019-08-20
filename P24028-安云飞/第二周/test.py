# -*- coding:utf8 -*-


# 简易计算器
while True:
    n1 = float(input('Please enter a number >>> '))
    s = input('please enter "+ - * /">>> ')
    n2 = float(input("Please enter a number >>>"))

    if s == "+":
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif s == "-":
        print('{} - {} = {}'.format(n1, n2, n1 - n2))
    elif s == "*":
        print('{} * {} = {}'.format(n1, n2, n1 * n2))
    elif s == "/":
        print('{} / {} = {}'.format(n1, n2, n1 / n2))
    else:
        print("your input is not number.")




