#### 理解并发与并行

并发：爆发，爆炸，可以先想象一下这类词汇，并发与之相同，是要在一定时间内要处理大量的事务。比如把淘宝网想象成一台服务器，有10万人要在凌晨12点参与秒杀，10万个连接瞬间与这台服务器建立连接，这就是并发。

并行：平和，平缓，可以先想象一下这类词汇，并行与并发不同，它并不“激进”，而是有序的齐头并进的同时处理多个事务。比如再把淘宝想象成一台服务器，有10万人在同时在线浏览网站，服务器同时建立10万个连接服务这些人。

#### 理解线程与进程，并说明它们的应用场景

一个程序发起执行的实例即是进程，而线程又是进程的基本运作单位，进程是线程的容器。

程序是源码编译后的文件，存放在磁盘上。当程序被加载到内存中，就变成了进程。

在操作系统中，进程认为自己独占所有的系统资源，各个进程之间的资源并不共享。而线程则可以共享进程中的资源。

#### Python中的GIL是什么，它影响什么

GIL全称global interpreter lock，字面意思全局解释器锁。

它能保证解释器进程CPython中，同一时间只有一个线程在执行字节码。

官方原话是：The mechanism used by the CPython interpreter to assure that only one thread executes Python bytecode at a time.

#### 结合本周知识现实如下功能：

**创建两个线程，其中一个输出1-26，另外一个输出A-Z，要求最终程序输出格式为： 1A 2B 3C ...**

```python
import threading
import time


def num_print():
    for i in range(1, 27):
        alp_lock.acquire()
        print(i, end='')
        num_lock.release()
        time.sleep(0.2)


def alp_print():
    apl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in apl:
        num_lock.acquire()
        print(i),
        alp_lock.release()
        time.sleep(0.2)


num_lock = threading.Lock()
alp_lock = threading.Lock()
num = threading.Thread(target=num_print)
alp = threading.Thread(target=alp_print)
num_lock.acquire()
num.start()
alp.start()
num.join()

```

