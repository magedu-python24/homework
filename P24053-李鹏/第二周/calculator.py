# v-1
# 待优化的问题：实现用户退出程序；被除数不为0的特殊处理
while True:
    operator = ('+', '-', '*', '/')
    a = int(input('please input number:'))
    operate = input('please input an operator, eg. + - * /: ')
    b = int(input('please input another number:'))
    if operate == operator[0]:
        c = a + b
    elif operate == operator[1]:
        c = a - b
    elif operate == operator[2]:
        c = a * b
    elif operate == operator[3]:
        if b == 0:
            print('除数不能为0')
            break
        else:
            c = a/b
    print('result:', c)