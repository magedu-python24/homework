#### 一、内置的open函数打开文件有几种模式，它们的区别是什么？

| 模式 | 说明                                                         |
| :--: | :----------------------------------------------------------- |
|  r   | 读取模式（这是默认模式）                                     |
|  w   | 写入模式，但是会将文件内容清空                               |
|  x   | 创建模式，但是文件如果已经存在，会返回失败                   |
|  a   | 追加模式，会将内容追加到文件末尾如果文件存在的话             |
|  b   | 二进制模式                                                   |
|  t   | 文本模式（这是默认模式）                                     |
|  +   | 可以理解为补充模式，如'w+b'是二进制写入模式，同时具备两种模式的能力。 |



#### 二、使用base64解码“bWFnZWR1LmNvbQ==”，使用base64编码”magedu.com”，分别给出它们的解码和编码结果。

```python
import base64
base64.b64decode('bWFnZWR1LmNvbQ==').decode() # output: 'magedu.com'
base64.b64encode('magedu.com'.encode()) # output: b'bWFnZWR1LmNvbQ=='
```



#### 三、列出本周讲的几种序列化方法，它们各自的特点是什么?

**pickle库的序列化方法及特点：**

- dumps: 将对象序列化为bytes对象
- dump：将序列化对象写入到一个文件中
- loads：将bytes对象反序列化，也就是恢复到内存中
- load：将文件中读取到的数据反序列化

**序列化应用：**

- json: 应用广泛，轻量级，几乎所有编程语言都支持
- MessagePack: 比json更加高效，适用于大部分编程语言



#### 四、写一个脚本实现找到/tmp目录及其子目录下的以.htm结尾的文件，把其后缀名改为.html

```python
from pathlib import Path
from pathlib import PurePath


def rename(path):
    p = Path(path)
    for i in p.glob('**/*.htm'):
        i.rename(PurePath(i).with_suffix('.html'))
        print('{} has changed to {}'.format(i, PurePath(i).with_suffix('.html')))


rename('/tmp')
```

