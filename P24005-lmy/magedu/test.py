'''num = int(input('>>>'))
if num >= 1000:# 判断一个数有几位，并打印
    if num >= 10000:
        length = 5
    else:
        length = 4
else:
    if num >= 100:
        length = 3
    elif num >= 10:
        length = 2
    else:
        length = 1
print('length=', length)
avl1 = num
x = 10 ** (length-1)
for i in range(length):
    print(avl1 // x , end=' ') # 从高位到低位打印
    avl1 %= x
    x //= 10
print()
avl2 = num
for i in range(length):
    print(avl2 % 10, end=' ')
    avl2 = avl2 // 10
'''
n = int(input('>>>'))
for i in range(n-2):
    if i == 0:
        print('*' * n)
    print('*'+' '*(n-2)+'*')
else:
    print('*' * n)

