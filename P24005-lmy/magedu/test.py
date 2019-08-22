# 判断一个数有几位，并打印  折半思想
'''
num = int(input('>>>'))
if num >= 1000:
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
'''
# 上题延续：# 从高位到低位打印
'''
avl1 = num
x = 10 ** (length-1)
for i in range(length):
    print(avl1 // x , end=' ') 
    avl1 %= x
    x //= 10
'''
# 上题延续：# 从低位到高位打印
'''
avl2 = num
for i in range(length):
    print(avl2 % 10, end=' ')
    avl2 = avl2 // 10
'''
# 判断学生成绩，成绩等级A~E.其中，90分以上的为A，80~89分的为B，70~79分的为C，60~69分的为D，60分以下的为E
'''
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
'''
# 输出一个数，打印出以这个数为边的正方形
'''
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
'''
# 1~5的阶乘之和
'''
x = 1
y = 0
for i in range(1, 6):
    x *= i
    y += x
    print(x, y)
'''
# 求100以内所有奇数的和
'''
y = 0
for i in range(1, 100, 2):
    y += i
print(y)
'''
# 给一个数，判断是否为素数 ==>素数只能被1和它本身整除
'''
n = int(input('>>>'))
for i in range(2, n):
    if n % i == 0:
        print(n, 'is not a prime number')
        break
else:
    print(n, 'is a prime number')
'''
# 给一个半径，求圆的面积和周长
'''
import math
r = float(input('>>>'))
x = math.pi * r ** 2
y = math.pi * r * 2
print(x, y)
'''
# 输入两个数，比较大小后，从小到大升序打印
'''
x = int(input('>>>1'))
y = int(input('>>>2'))
if x > y:
    print(y, x)
else:
    print(x, y)
'''
# 依次输入若干个整数，打印出最大值。如果输入为空，则退出
'''
firstnum = input('>>>')
if firstnum != '':
    print(firstnum)
    while 1:
        num = input('>>>')
        if num:
            num = int(num)
            firstnum = int(firstnum)
            if firstnum < num:
                firstnum = num
            print(firstnum)
        else:
            break
'''
# 三元表达式
'''
a = 1
b = 0
if a > b:
    print(a)
else:
    print(b)
print(a) if a > b else print(b)  # 三元表达式写法
'''
# 输入n个数，求每次输入后的算术平均数
'''
result = 0
count = 0
while 1:
    num = input('>>>')
    if num != '':
        num = int(num)
        result += num
        count += 1
        print('sum is', result)
        print('average is', result/count)
    else:
        break
'''
# 打印九九乘法表
'''
# 方法一
for i in range(1, 10):
    line = ''
    for j in range(1, i+1):
        avl = i * j
        if j > 1 and avl < 10:
            avl = str(avl) + ' '
        line = str(j) + '*' + str(i) + '=' + str(avl) + ' '
        print(line, end='')
    print()
# 方法二
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}*{}={:<{}}'.format(j, i, i * j, 1 if j < 2 else 2), end=' ')
    print()
# 方法三
for i in range(1, 10):
    for j in range(i, j+1):
        print('{}*{}={:<2}'.format(i, j, i*j), end=' ')
    print()
# 方法四
for i in range(1, 10):
    print(' '*7*(i-1), end='')
    for j in range(i, 10):
        print('{}*{}={:<2}'.format(i, j, i*j), end=' ')
    print()
# 方法五 =====> 将一行视为一个整体，然后整体右对齐
for i in range(1, 10):
    line = ''
    for j in range(i, 10):
        line += '{}*{}={:<{}}'.format(i, j, i*j, 2 if j < 4 else 3)
    print('{:>60}'.format(line))
'''
# 输入一个数，打印最长为这个数的菱形 ====> 对称，range（-3, 4）
'''
# 方法一
n = int(input('>>>'))
for i in range(-n//2+1, n//2+1):
    print(' '*abs(i) + '*'*(n-abs(i)*2))
# 方法二
n = int(input('>>>'))
e = n // 2
for i in range(-e, e+1):
    for j in range(1, n+1):
        if abs(i) < j < n-abs(i)+1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
# 方法三  ==> 坐标系思路，即：x轴和y轴的坐标值加起来，小于x或者y。但是该方式如果图形不对称，则打印不准确
n = int(input('>>>'))
e = n // 2
for x in range(-e, e+1):
    for y in range(-e, e+1):
        if abs(x) + abs(y) == e:
            print('*', end='')
        else:
            print(' ', end='')
    print()
'''
# 打印对顶三角形
'''
# 方法一
n = int(input(">>>"))
e = n // 2
for i in range(-e, e+1):
    print(' ' * (e - (abs(i))) + '*' * (abs(i) * 2 + 1))
# 方法二
n = int(input(">>>"))
e = n // 2
for y in range(e, -e-1, -1):
    for x in range(-e, e+1):
        if  abs(y) >= abs(x):
            print('*', end='')
        else:
            print(' ', end='')
    print()
'''
#  打印闪电
'''
# 方法一
n = 7
for y in range(3, -4, -1):
    for x in range(-3, 4):
        if (x <= 0 <= y or y <= 0 <= x) and abs(x) + abs(y) < 4:
            print('*', end='')
        else:
            print(' ', end='')
    print()
# 方法二
n = 7
for i in range(-3, 4):
    if i < 0:
        print(' ' * abs(i) + '*' * (4 - abs(i)))
    elif i > 0:
        print(' ' * abs(3) + '*' * (4 - abs(i)))
    else:
        print('*' * n)
'''
# 斐波那契数列：求100以内。=====> 一个数列从第三项项开始，每个数等于前两项之和
'''
x = 0
y = 1
while 1:
    fib = x + y
    if fib > 100:
        break
    print(fib)
    x, y = y, fib  # ==> x = y ; y = fib
'''
# 斐波那契数列：求第101项
'''
x = 1
y = 1
count = 2
while count < 101:
    fib = x + y
    count += 1
    x, y = y, fib  # ==> x = y ; y = fib
print(count, fib)
'''
# 求10万以内所有质数  ====> 质数：大于1的自然数，只能被1和本身整除的数
'''import datetime
start = datetime.datetime.now()
l = [2]
for i in range(3, 100000, 2):  # 从3开始，剔除偶数，===》缩小范围，减少遍历
    for j in range(3, int(i**0.5) + 1, 2):  # 从3开始=》剔除偶数，因为奇数不能被偶数整除=》开方范围减半=》以防万一范围+1
        if i % j == 0:
            break
    else:
        l.append(i)
print((datetime.datetime.now() - start).total_seconds())
print(len(l))
'''

