# 4. 使用选择排序算法实现排序[3, 5, 1, 7, 9, 6, 8]
lst = [3, 5, 1, 7, 9, 6, 8]
lenlst = len(lst) #列表长度，用于迭代次数
for i in range(lenlst) :
   lst_min = i
   for j in range(i+1,lenlst) :
      if lst[j] < lst[lst_min] : #找出最小数，放首位
         lst_min = j
   if i != lst_min :
      lst[i] ,lst[lst_min] = lst[lst_min] ,lst[i]  #换位置
print(lst)

# 5. 有如下一个字符串变量logs，请统计出每种请求类型的数量（提示：空格分割的第2列是请求类型），得到如下输出：
# POST 2
# GET 3
# 下边是logs变量：
logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200
'''
logs = logs.replace('"',' ').lower().strip()
lst2 = [] #定义一个空列表，目的是取logs的第二列
lst_logs = logs.splitlines() #按行切分，返回列表
lenlst  = len(lst_logs)
for i in range(lenlst) : #把列表的每一项单独出来，相当于logs的每一行,
   lst = lst_logs[i].split() #按空格切分每一行
   lst2.append(lst[1]) #取每一行的第二列放到空列表lsts中
post = lst2.count('post')
get = lst2.count('get')
print('post',post)
print('get',get)





