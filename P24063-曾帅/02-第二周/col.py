while True:
        a = float(input('please input a number:'))
        b = input('please input an operator(example:+ - * /):')
        c = float(input('please input a  number again:'))
        if b == '+':
            print(a + c)
        elif b == '-':
            print(a - c)
        elif b == '*':
            print(a * c)
        elif b == '/':
            print(a / c)
        else:
            print('ERROR: please input a normal operator')
            continue