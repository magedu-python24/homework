###  1、什么是高阶函数和柯理化并举例说明。 

**高阶函数：以函数做为参数或输出一个函数的函数，或者前面两个条件同时满足的函数，称之为高阶函数**。

例如：

```python
def add(x, y):
    return x + y

def count(x, y, add):
    return add(x, y)

# count函数把add函数做为参数，因此count是一个高阶函数
count(5, 6, add)
```



**柯理化：将原本接收两个参数的函数，转化成接收一个参数的函数。新的函数会返回以原来第二个参数做为参数的函数，如：**

```python
# 原函数
def add(x, y):
    return x + y
# 原函数的调用
add(5,6)
# 转换为柯里化函数
def add(x):
    def _add(y):
        return x + y
    return _add
# 柯里化函数的调用
add(5)(6)
```



### 2、请列出functools包内的每个函数的功能作用。 

functools.cmp_to_key(func):  将老格式的比较函数转换为主要函数

@functools.lru_cache(maxsize=128, typed=False): 一个缓存函数，当一个函数被缓存时，再次调用将直接返回结果，节省时间

@functools.total_ordering:  为一个丰富的类定义排序方法提供其余的内容。

functools.partial(func, *args, **keywords):  返回一个新的partial object, 调用时类似于函数调用，还有参数和关键字参数

class functools.partialmethod(func, *args, **keywords):  返回一个新的partialmethod描述符，它的行为类似于partial，只是它被设计为用作方法定义，而不是直接调用。 

functools.reduce(function, iterable[, initializer]) :  从左到右，将两个参数的函数累积应用到序列项上，使序列减少到一个值。 

@functools.singledispatch: 将一个函数转换为single-dispatch generic function.

functools.update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES) :  更新装饰器中的各种属性，以致于被装饰对象属性不被改变

@functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES): 调用update_wrapper()

###  3、使用已学习的装饰器相关知识自己实现functools.lur_cache。

```python
import inspect
from functools import wraps


def make_cache(fn):
    def _cache(*args, **kwargs):
        cache = {}
        @wraps(fn)
        def make_key():
            sig = inspect.signature(fn)
            params = sig.parameters
            param_names = [key for key in params.keys()]
            param_dict = {}
            for i, v in enumerate(args):
                k = param_names[i]
                param_dict[k] = v
            param_dict.update(kwargs)
            for i, v in params.items():
                if i not in param_dict.keys():
                    param_dict[i] = v.default
            return tuple(sorted(param_dict.items()))
        key = make_key()
        if key not in cache.keys():
            cache[key] = fn(*args, **kwargs)
        return cache[key]
    return _cache


@make_cache
def add(a, b):
    return a + b


print(add(1, 8))

```

###   4、什么是类型注解并说明其背后的目的。  

```python
def add(x:int, y:int):
    return x + y
```

在参数后标注参数的数据类型，表明该参数在传值时的数据类型。但即便如此，python仍然无法约束传值的类型，即使x声明需要传入int类型，但传入string类型也不会报错。类型注解的目的只是一个辅助说明，可以传给第三方工具用来检查代码中的错误，但在实际运行过中当中，并不能对传入的数据类型做任何约束。