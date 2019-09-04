

while True:
    a=input('num1>>')
    opt=input('operator>>')
    b=input('num2>>')
    c=0
    if opt=='*':
        c=int(a)*int(b)
    elif opt=='/':
        c=int(a)/int(b)
    elif opt=='+':
        c=int(a)+int(b)
    elif opt=='-':
        c=int(a)-int(b)
    else:
        print('unrecognized option')
        continue
    print('{}{}{}={}'.format(a,opt,b,c))


