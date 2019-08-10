# 思路：
# 找出列表中最大的值 然后将该值 移动到末尾 该位置的值替换为末尾的值
# pop 列表 将该值传到另外列表1中
# 找出列表中最大的值 然后将该值 移动到末尾 该位置的值替换为末尾的值
# pop 列表 将该值传到另外列表1中
# 找出列表中最大的值 然后将该值 移动到末尾 该位置的值替换为末尾的值
# pop 列表 将该值传到另外列表1中
# 。
# 。
# 。
# 。



# list1 = [3, 5, 1, 7, 9, 6, 8]
# list2 = []
#
# while list1:
#     LarNum = list1[0]
#     LarNumInd = 0
#     for i in range(1,len(list1)):
#         if list1[i] > LarNum:
#             LarNum = list1[i]
#             LarNumInd = list1.index(LarNum)
#     list1[LarNumInd] = list1[-1]
#     list1[-1] = LarNum
#     list1.pop()
#     list2.append(LarNum)
#
# list2.reverse()
# print("重新排列后的数组为：")
# print(list2)
#


logs = '''

111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200

111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200

111.13.100.92 "Post /mock/login/ HTTP/1.1" 200

223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200

111.30.144.7 "GET /mock/users/ HTTP/1.1" 200

'''

# PostNum = 0
# GetNum = 0
# ListLog = logs.splitlines()
# for i in ListLog:
#     if len(i) < 1:
#         ListLog.remove(i)
# ListLog.pop()
# print(ListLog)
#
# for str in ListLog:
#     print(str)
#     LogSplit = str.split()
#     print(LogSplit)
#     print(LogSplit[1])
#     ActionType = LogSplit[1]
#     ActionType = ActionType.lower()
#     print(ActionType)
#     if "post" in ActionType:
#         PostNum += 1
#     else:
#         GetNum += 1
# print("POST ",PostNum)
# print("GET ",GetNum)
#
# str = '111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200'
#
# LogSplit = str.split()  #['111.30.144.7', '"POST', '/mock/login/?t=GET', 'HTTP/1.1"', '200']
# Type = LogSplit[1].lower() #"post
# if "post" in Type:
#     print("POST")
# else:
#     print("Get")

PostNum = 0
GetNum = 0
ListLog = logs.splitlines()
for i in ListLog:
    if len(i) < 1:
        ListLog.remove(i)
ListLog.pop()

for str in ListLog:
    LogSplit = str.split()
    ActionType = LogSplit[1]
    ActionType = ActionType.lower()
    if "post" in ActionType:
        PostNum += 1
    else:
        GetNum += 1
print("POST ",PostNum)
print("GET ",GetNum)
