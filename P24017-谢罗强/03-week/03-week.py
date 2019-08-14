#03-week


1. 说明列表的浅拷贝和深拷贝的区别
2. 说明列表和元组的相同点和不同点
3. 请写出字符串支持的所有方法及说明（例如: lower 返回字符串的小写）
4. 使用选择排序算法实现排序[3, 5, 1, 7, 9, 6, 8]
5. 有如下一个字符串变量logs，请统计出每种请求类型的数量（提示：空格分割的第2列是请求类型），得到如下输出：
POST 2
GET 3
下边是logs变量：
logs = '''
111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200 
111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200 
111.13.100.92 "Post /mock/login/ HTTP/1.1" 200 
223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200 
111.30.144.7 "GET /mock/users/ HTTP/1.1" 200 
''' 

A:
1. 列表浅拷贝对于容器类型元素只会拷贝对象引用即内存地址，深拷贝则是完全拷贝副本，新的元素地址
2. 列表和元组相同点：可迭代，可索引，线性序列
             不同点：列表可变，元组不可变
3. 字符串str所有方法：
    str.index(subs) #返回第一个子串最小索引
4. 选择排序算法实现如下：
def selectsort(src: list = None):
    if not src:
        src = [3, 5, 1, 7, 9, 6, 8]
    length = len(src)
    for i in range(length):
        for j in range(i+1, length):
            if src[j] < src[i]:
                src[j], src[i] = src[i], src[j]
    return(src)
5. 实现如下：
def countreqtype(src: str = None):
    target = {}
    if not src:
        src = '''
            111.30.144.7 "POST /mock/login/?t=GET HTTP/1.1" 200
            111.30.144.7 "Get /mock/users/?t=POST HTTP/1.1" 200
            111.13.100.92 "Post /mock/login/ HTTP/1.1" 200
            223.88.60.88 "GET /mock/users/?t=POST HTTP/1.1" 200
            111.30.144.7 "GET /mock/users/ HTTP/1.1" 200
            '''
    for line in src.splitlines():
        line = line.strip()
        if not line:
            continue
        reqtype = line.split()[1].lstrip('"').upper()
        target[reqtype] = target.get(reqtype, 0) + 1
    #return target
    for k, v in target.items():
        print('{} {}'.format(k, v))

