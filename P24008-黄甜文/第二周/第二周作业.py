# 4. 实现一个简易的计算器，效果如下：
#     （1）. 运行后提示让用户输入一个数字
#     （2）. 提示输入操作符（+ - * /）
#     （3）. 再次提示输入一个数字
#     （4）. 打印计算结果
#     （5）. 在不退出程序的前提下，可以允许用户继续输入新一组数据计
while True:
    num1 =int( input('请输入第一个数字：'))
    a = input('请输入+ - * /:')
    num2 = int(input('请输入第二个数字：'))
    if a == '+':
        num = num1 + num2
    elif a == '-':
        num = num1 - num2
    elif a == '*':
        num = num1 * num2
    else:
        num = num1 / num2
    print(num)


