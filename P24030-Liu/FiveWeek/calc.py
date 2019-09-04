def counter(a,opt,b):
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
        c=None
    return c


while True:
    a=input('num1>>')
    opt=input('operator>>')
    b=input('num2>>')
    c=counter(a,opt,b)
    if c==None:
        print('opt error')
    else:
        print('{}{}{}={}'.format(a,opt,b,c))
    if 'q'==input('q exit,other key continue:'):
        break;


