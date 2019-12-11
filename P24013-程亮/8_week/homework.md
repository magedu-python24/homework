#### 一、使用本周和之前所学习的知识实现cat命令（支持查看内容和-n参数功能即可）

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('file', help='which file do you want to show')
parser.add_argument('-n', action='store_true', help='output with line number')


def cat(path, ln=False):
    with open(path) as f:
        num = 1
        for i in f:
            print('\t{}\t{}'.format(num, i), end='') if ln else print(i, end='')
            num += 1


args = parser.parse_args()
cat(args.file, args.n)

```



#### 二、有字符串”not 404 found 张三 99 深圳”，使用正则过滤掉英文和数字，最终得到”张三 深圳”

```python
for i in re.findall('[^a-z0-9 ]+', 'not 404 found 张三 99 深圳'):
    print(i, end=' ')
# output: 张三 深圳 
```



#### 三、结合本周所讲的知识，总结如何设计一个日志分析系统，分析可能遇到问题和解决方法（文字阐述） 

日志收集：将需要的内容从服务程序的日志中过滤出来进行周期性收集，以每天的日期时间做为文件名，如2019-12-11.txt,  然后打包压缩存放的共享存储目录中。 

日志存储：使用一台独立的服务器，挂载一个超大容量的硬盘用来存储收集来的日志，提供一个接口来分发日志，起到缓冲作用。

日志分析：使用另一台服务器，运行分析程序从分发接口获取日志并进行分析，将分析结果保存在数据库中。

日志展示：从数据库中读取分析结果，结合web进行图表展示。



可能遇到的问题：

1、日志收集的太多，分析不过来，这时候可以多加几台分析程序的服务器。

2、独立在服务器有单点故障的风险，如果突然挂掉，那消息队列的角色就没有了，会影响整个分析过程，这时候可以使用分布式文件存储集群，分发日志的程序也分散在其它节点上。

3、整体调整困难大，不易于维护。收集程序，分析程序，分发接口都是分开的，之后学习更高级的内容，应该可以解决，调整更灵活。

4、web图表展示目前做不到，等学完前端应该可以。