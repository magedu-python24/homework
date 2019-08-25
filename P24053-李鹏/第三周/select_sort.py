# 使用选择排序算法实现排序[3, 5, 1, 7, 9, 6, 8]
# collection = [3, 5, 2, 7, 2, 6, 8]
collection = [3, 5, 1, 7, 9, 6, 8]
length = len(collection)
for i in range(length - 1):
    least = i
    for k in range(i + 1, length):
        if collection[k] < collection[least]:
            least = k
        collection[least], collection[i] = collection[i], collection[least]
print(collection)


# 字符串处理
# 第5题
"""
字符串变量logs如下，请统计出每种请求类型的数量
"""
logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 
''' 
count = [0] * 2
loglst = logs.splitlines()
for i in loglst:
    if i == '':continue
    elif i.find('POST', 10, 20) > -1:
        count[0] += 1
    elif i.find('Post', 10, 20) > -1:
        count[0] += 1
    elif i.find('GET', 10, 20) > -1:
        count[1] += 1
    elif i.find('Get', 10, 20) > -1:
        count[1] += 1

print('POST-{}, GET-{}'.format(count[0], count[1]))

# 思考：时间复杂度，对于logs中每个元素，都需要执行4次find ;find()的复杂度O(n)，整体时间复杂度O(n**2)
# 可优化