#### 1. 如何为函数定义keyword-only参数（写出个例子即可)？

```python
def kwonly(*args, city):
    info=list(args)
    info.append(city)
    return info

kwonly('lucas', 'learining', 'python3', city='beijing')
```

***

#### 2. 什么是LEGB，请解释?

> LEGB是四个单词的缩写，即L(local),E(enclosing),G(global),B(build-in), 表示的是变更名解析的顺序。  

> > 在python环境中，函数的变量仅限于函数可见，外部看不到，这个是local变量。

> > enclosing即为闭包，嵌套函数中内层函数引用到了外层函数的变量。

> > global是全局作用域，是一个模块的命名空间，模块导入时创建，解释器退出时销毁

> > build-in是Python内置模块的命名空间，紧随解释器的生命周期。如print, str, list等。

***

#### 3. 二叉树的性质

每个节点最多2棵子树

> 二叉树不存在度数大于2的结点

它是有序树，左、右子树都是顺序的，不能交换次序

即使某个结点只有一棵子树，也要确定它是左子树还是右子树

#### 4. 使用本周学习的技术改造第二周的计算器实现，其目标如下：

1. 运行后提示让用户输入一个数字

2. 提示输入操作符（+ - * /）

3. 再次提示输入一个数字

4. 打印计算结果

5. 在不退出程序的前提下，可以允许用户继续输入新一组数据计

6. 尽可能改善用户体验（新需求） 

```python
def counter(a,op,b):
    if op == '+':
        return int(a) + int(b)
    elif op == '-':
        return int(a) - int(b)
    elif op == '*':
        return int(a) * int(b)
    elif op == '/':
        return int(a) / int(b)
    else:
        return 'wrong input'
while True:
    print('input <quit> in first number to quit.')
    a=input('input a number: ')
    if a=='quit':
        print('bye bye...')
        break
    op=input('input opearter like +,-,*,%: ')
    b=input('input second number: ')
    print(counter(a,op,b))
```

