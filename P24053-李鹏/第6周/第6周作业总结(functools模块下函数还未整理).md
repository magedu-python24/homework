#第6周总结
###1. 什么是高阶函数和柯理化并举例说明。
满足以下其中一点的函数称为 高阶函数：

	1.接收一个或者多个函数作为参数
	2.返回一个函数

	def reg(cmd):
    	def _reg(fn):
        	commands[cmd] = fn
        return fn
    return _reg

柯里化：指将原来接收两个参数的函数 变成 一个新的接收一个参数的过程;该函数返回内层函数

	def add(x, y):
		return x + y

柯里化为：

	def add(x):
		def _add(y):
			return x+y
		return _add


###2.请列出functools包内的每个函数的功能作用。

	总结中...

###3. 请使用已学习的装饰器相关知识自己实现functools.lur_cache。
思路：

	#1.构建(由函数传参组成)key: 处理位置参数 -> 处理关键字参数 -> 处理默认值
	#2.把函数入参 和 出参作为key-value 存入 local_cache字典；下次调用函数，若key相同，直接取缓存（local_cache）存储的结果；key不同则存入缓存
	#3.增加定期清除缓存的动作，在存入缓存时，把当前【时间戳】 + 【函数返回值】 整体存入value; 在每次调用时，判断是否需要把【缓存中的数据】放入 【待释放列表中】后，执行释放缓存
	#4.问题：还未考虑缓存空间大小问题

	from functools import wraps, lru_cache
	import inspect
	import datetime
	import time

	def mag_cache(fn):
    	local_cache = {}
    	@wraps(fn)
    	def wrapper(*args, **kwargs):
        	def _clear_expire ( ) :
            	# 缓存清除
            	expire_key = [ ]
            	for k , v in local_cache.items ( ) :
                	ret , stamp = v  # 在for循环时，可以直接解构元组
                	if datetime.datetime.now ( ).timestamp ( ) - stamp > 5 :
                    	expire_key.append ( k )
            	for k in expire_key :
                	local_cache.pop ( k )
        	_clear_expire ( )

        def _make_key ( args , kwargs ) :
            # 参数处理，构建key
            sig = inspect.signature ( fn )
            params = sig.parameters  # 返回的是一个有序字典
            # print(type(params), params)
            # print(params.keys())
            params_dict = { }
            values = list ( params.values ( ) )
            keys = list ( params.keys ( ) )
            # 处理位置参数传参-1
            # for i, v in enumerate(args):
            #     params_dict[keys[i]] = v
            # 简化上述代码-1
            params_dict.update ( zip ( params.keys ( ) , args ) )  # 为什么这么简化？
            # 处理关键字传参-2
            # for k,v in kwargs.items():
            #     params_dict[k] = v
            # 简化上述代码-2
            params_dict.update ( kwargs )  # 为什么这么简化？
            # 处理缺省值
            for k , v in params.items ( ) :
                if k not in params_dict :
                    params_dict [ k ] = v.default
            key = tuple ( sorted ( params_dict.items ( ) ) )
            print ( key )
            return key
        key = _make_key ( args , kwargs )

        if key not in local_cache:
            local_cache[key] = (fn(*args, **kwargs), datetime.datetime.now().timestamp())

        ret = local_cache[key]
        return ret
    return wrapper

### 4. 什么是类型注解并说明其背后的目的。
类型注解：在函数定义时，说明函数入参 和 出参 的数据类型；目的是为了解决python作为动态语言的弊端：变量可以随时被赋值，并赋值成跟原本设想不同的数据类型；

函数参数检查装饰器：
	1.在调用函数前，调用检查函数 -> 2.将函数作为参数，传入检查函数中，检查实际传参数据类型和声明对比