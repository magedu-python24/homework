'''num = int(input('>>>'))
if num >= 1000:# 判断一个数有几位，并打印  折半思想
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

# 判断学生成绩，成绩等级A~E.其中，90分以上的为A，80~89分的为B，70~79分的为C，60~69分的为D，60分以下的为E
x = int(input('>>>'))
if x >= 90:
    y = 'A'
elif x >= 80:
    y = 'B'
elif x >= 70:
    y = 'C'
elif x >= 60:
    y = 'D'
else:
    y = 'E'
print(y)

# 输出一个数，打印出以这个数为边的正方形
n = int(input('>>>')) # 方法一
for i in range(n):
    if i == 0 or i == n-1:
        print('*' * n)
    else:
        print('*'+' '*(n-2)+'*')

n = int(input('>>>')) # 方法二  对称写法
x = -n // 2
for i in range(x, x+n):
    if i == x or i == x+n-1:
        print('*'*n)
    else:
        print('*'+' '*(n-2)+'*')

# 1~5的阶乘之和
x = 1
y = 0
for i in range(1, 6):
    x *= i
    y += x
    print(x, y)

# 求100以内所有奇数的和
y = 0
for i in range(1, 100, 2):
    y += i
print(y)

# 给一个数，判断是否为素数----素数只能被1和它本身整除
n = int(input('>>>'))
for i in range(2, n):
    if n % i == 0:
        print(n, 'is not a prime number')
        break
else:
    print(n, 'is a prime number')

'''



