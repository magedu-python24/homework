#### 根据本周异常相关视频，总结try/except/else/finally的用法及如何自定义异常

```python
try: # try 代码块包含希望捕获异常的代码片断
    1/0
except ZeroDivisionError: # except 代码块定义可能出现的错误类型及相应操作
    print('error happen')
else: # else 代码块是指没有发生任何异常时执行的操作
    print('everything ok')
finally: # finally 代码块是指无论上面的代码发生了什么情况，这里一定会执行的操作
    print('always execute.')
```

自定义异常

```python
class SysErr(Exception): # 自定义异常须从Exception继承
    pass

try:
    pass
except SysErr: # 此时except捕获自定义异常相关的错误
    print('get the error.')
finally:
    print('do some clean jobs')
```

------



#### 实现个插件化开发的demo

```python
# t1.py
class GetInfo:
    def __init__(self):
        self.info = []

    def showinfo(self, info):
        self.info.append(info)
        return self.info

 # t2.py 简单的示例，实际应用会考虑很多情况
import importlib

if __name__ == '__main__':
    mod = importlib.import_module('t1')
    cls = getattr(mod, 'GetInfo')
    print(cls().showinfo('test...'))

```

------



#### 列出视频中讲到的git支持各个命令及说明 

git子命令说明，子命令的详细用法请参见git \<sub command\> --help

| 子命令   | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| init     | 将当前的目录初始化为一个git仓库                              |
| add      | 将文件添加到缓存区                                           |
| status   | 查看仓库的当前状态                                           |
| commit   | 将暂存区的改动提交到仓库中                                   |
| diff     | 查看两个版本文件之间的差异                                   |
| checkout | 将指定的文件或commit号或仓库等检出到工作区                   |
| reset    | 见名知意，是重置文件用的，具体用法见git reset --help，非常危险的命令，慎用 |
| reflog   | 显示commit的日志，所有的HEAD变法，都可以用这个命令查看到     |
| mv       | 可以更改暂存区文件的文件名                                   |
| rm       | 会在仓库和暂存区删除文件                                     |
| push     | 将本地仓库推送到远程仓库中                                   |
| config   | 配置全局或当前仓库的设置，如果用户名，邮箱等                 |
| remote   | 查看远程仓库                                                 |
| clone    | 将远程仓库克隆到本地                                         |

