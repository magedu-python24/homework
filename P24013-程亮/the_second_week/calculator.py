#！/bin/env python3

while True:
	a=input('please input a number: ')
	if not a:
		break
	opt=str(input('please input an operator, such as * / + -, keep space will exit: '))
	b=input('please input another number: ')
	if opt=='*':
		print('result is',int(a)*int(b))
	elif opt=='/':
		print('result is',int(a)/int(b))
	elif opt=='+':
		print('result is',int(a)+int(b))
	elif opt=='-':
		print('result is',int(a)-int(b))
	else:
		print('operator is wrong, please try again.')