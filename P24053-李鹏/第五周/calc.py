# 第五周作业：用函数简单实现计算器
# 异常情况处理：如果用户输入数字时，输入其他字符怎么处理？
def calculator(a, b, operate):
    operator = ('+', '-', '*', '/')
    if operate == operator[0]:
        c = a + b
    elif operate == operator[1]:
        c = a - b
    elif operate == operator[2]:
        c = a * b
    elif operate == operator[3]:
        if b == 0:
            print('除数不能为0')
        else:
            c = a/b
    return c

while True:
    a = int(input('please input number:'))
    operate = input('please input an operator, eg. + - * /: ')
    b = int(input('please input another number:'))
    c = calculator(a, b, operate)
    if c == None:
        print("calculate error")
    else:
        print("{}{}{}={}".format(a,operate,b,c))
    if 'q'==input('q exit,other key continue:'):
        break;