
while 1:
    x = int(input('please input a number：'))
    op = input('please input（+、-、*、/）：')
    y = int(input('please input another number：'))
    if op == '+':
        print(x + y)
    elif op == '-':
        print(x - y)
    elif op == '*':
        print(x * y)
    elif op == '/':
        if y != 0:
            print(x / y)
        else:
            print('input error')
    else:
        print('input error')


