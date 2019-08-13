while True:
    num1 = input("请输入第一个数字")
# isdigit判断输入的是否是一个整数，不是在重新输入
    if not num1.isdigit():
        print('输入内容必须为整数！！！！\n再来一次吧\n')
        continue

    else:
        num1 = int(num1)
# str用字符串类型转义
    opt = str(input('请输入操作符+-*/'))
# 用一个列表将字符加减乘除放进去
    opt_list = ['+', '-', '*', '/']
    if opt not in opt_list:
        print('请输入 + - * /')
        continue
    num2 = input("请输入第二个数字")
    if not num2.isdigit():
        print('输入内容必须为整数！！！！\n再来一次吧\n')
        continue
    else:
        num2 = int(num2)
    if opt == '+':
        result = num1 + num2
    elif opt == '-':
        result = num1 - num2
    elif opt == '*':
        result = num1 * num2
    elif opt == '/':
        result = num1 / num2

