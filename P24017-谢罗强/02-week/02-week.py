#02-week


1. 简要说明Python垃圾回收机制
2. 什么是斐波那契数列、素数、质数和猴子吃桃问题（文字说明即可）？
3. 请写出列表支持的所有方法及说明（例如: append 向列表末尾添加元素）
4. 实现一个简易的计算器，效果如下：
    （1）. 运行后提示让用户输入一个数字
    （2）. 提示输入操作符（+ - * /）
    （3）. 再次提示输入一个数字
    （4）. 打印计算结果
    （5）. 在不退出程序的前提下，可以允许用户继续输入新一组数据计


A:
1. Python垃圾回收机制：引用计数为0的对象在合适的时机会被pvm回收该对象的内存
2. 斐波那契数列：第0项为1，第1项为1，此后项是前两项之和
   素数：紧能被1和自身整除的正整数，最小素数为2
   猴子吃桃：共有n颗，每天吃n/2 + 1颗，第十天只剩1颗
3. 列表list：
       list.insert(index, value)
       list.append(value)
       list.pop([index]) #弹出index索引的值，不指定index则默认弹出最后一个，并返回value
       list.remove(value) #移除第一个value，无返回
       list.clear()
       list.copy()
       list.extend(iterable) #就地追加
       list.index(value, [start, [stop]]) #返回第一个value的索引，需要遍历
       list.count(value) #返回value在列表中出现的次数
       list.reverse()
       list.sort(key=None, reverse=False)  #就地排序
4. 代码如下：
def simple_arithmetic(x=None, y=None, sign=None):
    while True:
        while not x:
            try:
                x = int(input('first number:').strip())
            except Exception:
                print('无效输入,请输入一个整数')
        while not y:
            try:
                y = int(input('second number:').strip())
            except Exception:
                print('无效输入,请输入一个整数')
        while not sign:
            sign = input('arithmetic sign:').strip()
            if sign == '+':
                value = x + y
            elif sign == '-':
                value = x - y
            elif sign == '*':
                value = x * y
            elif sign == '/':
                value = x / y
            else:
                sign = ''
                print('无效输入,请输入运算符[+-*/]')
            print(value)
        x, y, sign = None, None, None
