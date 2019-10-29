# 4. 结合本周知识现实如下功能：
#创建两个线程，其中一个输出1-26，另外一个输出A-Z
#要求最终程序输出格式为： 1A 2B 3C ...
from threading import Thread,Barrier
from concurrent.futures import ThreadPoolExecutor



def Letter():
    letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return letter


def Number():
    number = [x for x in range(1,27)]
    return number

#bar = Barrier(2)
if __name__ == '__main__':
    with ThreadPoolExecutor(2) as T:
        t1 = T.submit(Letter)
        t2 = T.submit(Number)
        #print(t1.result())
        #print(t2.result())
        for x,y in zip(t2.result(),t1.result()):
            print(str(x)+y)
print('========end==============')


