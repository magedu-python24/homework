# -*- coding:utf8 -*-

"""
    使用本周学习的技术改造第二周的计算器实现，其目标如下：
     1. 运行后提示让用户输入一个数字
     2. 提示输入操作符（+ - * /）
     3. 再次提示输入一个数字
     4. 打印计算结果
     5. 在不退出程序的前提下，可以允许用户继续输入新一组数据计
     6. 尽可能改善用户体验（新需求）
"""


def Calculator(x, opt, y):
    if opt == "+":
        return x + y
    elif opt == "-":
        return x - y
    elif opt == "*":
        return x * y
    elif opt == "/":
        return x / y
    else:
        print("请正确输入")


while True:
    x = float(input("请输入数字: "))
    opt = input("请输入+,-,*,/: ")
    y = float(input("请输入数字: "))

    resuilt = Calculator(x, opt, y)
    print(resuilt)
