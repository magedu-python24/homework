# -*- coding:utf8 -*-

# 使用选择排序算法实现排序[3, 5, 1, 7, 9, 6, 8]
lst = [3, 5, 1, 7, 9, 11, 8]

# 冒泡算法
for i in range(len(lst)):
    temp = i
    for j in range(i+1, len(lst)):
        if lst[temp] > lst[j]:
            temp = j
    lst[i], lst[temp] = lst[temp], lst[i]

print(lst)

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print(lst)


# 5

logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200
'''


