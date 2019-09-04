# import time
# def deco(func):
#     def wrapper():
#         startTime = time.time()
#         func()
#         endTime = time.time()
#         msecs = (endTime - startTime)*1000
#         print("time is %d ms" %msecs)
#     return wrapper
#
#
# @deco
# def func():
#     print("hello")
#     time.sleep(1)
#     print("world")
#
# func()


# Flag = False
# def login(fn):
#     # global Flag
#     def wrapper(*args):
#         global Flag
#         if args[0] == "hcong" and args[1] == "123":
#             Flag = True
#         else:
#             Flag = False
#         fn(*args)
#     return wrapper
#
# @login
# def japan(username,password):
#     # global Flag
#     if Flag:
#         print("欢迎来到岛国 龙泽拉多！")
#     else:
#         print("回家吧！")
#
# japan("hcong","123")


# fn1 = lambda x:x+1
# print(fn1(2))
#
# list1 = [x for x in range(10)]
# print(list1)


def fn1(fn,a,b):
    fn(a,b)
    print("形参中包含函数")

def fn2(name,hobby):
    print("说出你的名字",name,hobby)


fn1(fn2,"houcong","basketball")