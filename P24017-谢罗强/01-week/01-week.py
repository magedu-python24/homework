#written by xielq at 07.15 about 01-week exercises.


1. 通过本周的学习和自己查阅，你知道linux有哪些发行版本？
A:centos
  ubuntu
  tails

2. 按以下需求写出对应的执行命令：
   a. 使用zhangsan用户通过ssh的22端口登录服务器192.168.139.100
   b. 在系统根目录下创建目录 data
   c. 在data中新建a.sh 文件
   d. 在a.sh 中写入内容echo "hello magedu"
   e. 查看文件内容
   f. 删除在 b 步骤中创建的 data 目录
   g. 退出ssh登录 

A:
   a. ssh 192.168.139.100 -l zhangsan
      ssh zhangsan@192.168.139.100
      ssh -p 22 zhangsan@192.168.139.100
   b. mkdir /data
   c. touch /data/a.sh
   d. echo "hello magedu" > /data/a.sh
   e. cat /data/a.sh
   f. rm -rf /data
   g. exit
      logout
