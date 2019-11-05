# -*- coding:utf8 -*-

# print("Hello World")


# Print Multiplication table

# for i in range(1,10):
#     for j in range(1,10):
#         if j <= i:
#             print("{0}*{1}={2}".format(str(j), str(i), str(i * j)), end='\n')
#     print()

# for i in range(1, 10):
#     line = " "
#     for j in range(1, 10):
#         if j <= i:
#             line = line + ("{0}*{1}={2}".format(str(j), str(i), (str(i * j) + "\t")))
#     print(line)
#
#
# for i in range(1, 10):
#     line = " "
#     for j in range(1, i+1):
#         line += '{}*{}={}\t'.format(j, i, i * j)
#     print(line)

# for i in range(1, 10):
#     line = ""
#     for j in range(1, 10):
#         if j >= i:
#             line += '{} x {} = {}\t'.format(i, j, i * j)
#     print(line)

# for i in range(1, 10):
#     line = ""
#     for j in range(9, 0, -1):
#         if j >= i:
#             line += '{} x {} = {}\t'.format(i, j, i * j)
#     print(line)

# for i in range(9, 0, -1):
#     line = ""
#     for j in range(1, i):
#         # print(j)
#         if i >= j:
#             line += ("{}x{}={}\t".format(j, i, i*j))
#     print(line)

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("{}*{}={:<{}}".format(j, i, i * j, 2 if j < 2 else 3), end="")
#     print()

# 九九乘法表扩展
# for i in range(1, 10):
#     line = ' \t' * (i - 1) * 2
#     for j in range(i, 10):
#         line += ('{}*{}={}\t'.format(i, j, i * j))
#     print(line)

# 打印菱形
# for i in range(9, 1, -1):
#     line = ' ' * (i - 1)
#     for j in range(i, 10):
#         line += ('* ')
#     print(line)
#
# for i in range(1, 10):
#     line = ' ' * (i - 1)
#     for j in range(i, 10):
#         line += ('* ')
#     print(line)


# l = list()
#
# for i in range(3, 31):
#     if i % 3 == 0:
#         l.append(i)
# print(l)
