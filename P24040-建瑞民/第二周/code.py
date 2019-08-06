while True:
    num1 = input('plase input first num or ENTER exit: ')
    if not num1:
        print('exit')
        break
    else:
        num1 = int(num1)
    f = input('plase input +/-/*/\/: ')
    num2 = int(input('plase input seond num: '))

    if f=='+':
        value = num1+num2
    elif f=='-':
        value = num1-num2
    elif f=='*':
        value = num1*num2
    elif f=='/':
        if num2 == 0:
            print('err and exit')
            break
        else:
            value = num1/num2
    else:
        print('err')
    print(value)
