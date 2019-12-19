#### 一、什么是类和实例并说明他们之间的关系

**类**：A template for creating user-defined objects. Class definitions normally contain method definitions which operate on instances of the class. 

​       一个用户定义对象的模板，通常包含操作实例的类。

​      个人理解：像姑娘头上的发簪，这就是用来装饰（操作实例）的饰品（类），如果不插在头上，它将没有任何用处。

**实例**：A class instance is created by calling a class object .

​		一个类实例由调用类对象来产生。

​		个人理解：把发簪插（调用）在姑娘头上用来装饰（产生实例），此时姑娘更美了，这就是完成了实例化。发簪不用（定义类不调用），那它就没有任何用处（类要调用才有具体动作）。



**类与实例的关系**：类定义了具体的属性和方法的集合，只有调用了才会产生作用。就如上面发簪的例子，发簪本身就是一个类，不使用它，没有任何作用，把它插在头上，这才是实例，此时发簪才发挥了作用。



#### 二、类的实例方法、类方法和静态分别如何定义举例说明，并总结它们的应用场景

```python
# 定义Toy类
class Toy:
    # __init__: 初始化实例用的
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def info(self):
        print('your toy is {}==>{}'.format(self.name, self.size))
    #类方法：会把类自身做为参数进行输入，装饰器的作用，适用于需要与类交互的场景。
    @classmethod
    def shout(cls):
        cls.noise = 'wo'
        print('class have a new property, check the message {}'.format(dir(cls)))
    #静态方法： 不会把类自身做为参数输入，装饰器的作用，适用于无须与类交互的场景。
    @staticmethod
    def show():
        print('print noise property: {}'.format(Toy.noise))

#类实例化
dog = Toy('alen', 35)
dog.info()
dog.shout()
dog.show()

```



#### 三、MRO是什么，描述其查找顺序

Method Resolution Order(简称MRO)，python用来解决基类搜索顺序的算法，目前python3使用的是C3算法。当一个类被创建出来时，会有一个MRO有序列表（线性化且确定了顺序），搜索算法是深度优先，重复值只保留最后一个，解决了继承的单调性。

#### 四、Mixin是什么，描述其应用场景 

Mixin：当一个类功能非常复杂时，内部功能的实现是来自于不同的类，而不是一一自己实现，将不同的类组合起来实现相应的功能。实质上就是类的多态继承，进行组合设计。装饰器也可以实现增强功能，但缺点是不能继承，这时候就需要使用Mixin了。