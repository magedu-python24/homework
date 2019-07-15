# homework

## 马哥教育python实战24期

### 不要删除别人的代码！ 目录结构
                     
```
每次作业请创建单独的目录，例如
P24001-张三/第一周/学习计划.txt
P24001-张三/第一周/example.py
```

### 1.命令行添加代码
```
第一次使用：         
centos：       
  yum install git       
  
  
Ubuntu：       
  apt-get install git
  
git clone https://github.com/magedu-python24/homework.git

更新本地代码 git pull

查看代码状态 git status

后面添加代码，只需要下面三行即可：
  git pull //拉取最新的代码文件
  git add .     
  git commit -m "first commit" //第一次提交  
  git pull //提交之前，先同步下最新版的代码，避免冲突
  git push -u origin master //同步到远程服务器      

用命令行操作，要添加ssh的公钥到github里，操作方法

创建SSH key的方法很简单，执行如下命令就可以： ssh-keygen 生成的SSH key文件保存在中～/.ssh/id_rsa.pub

然后用文本编辑工具打开该文件，我用的是cat,所以命令是： cat ~/.ssh/id_rsa.pub

接着拷贝出现在屏幕上的内容，将它粘帖到github帐号管理中的添加SSH key界面中。 打开github帐号管理中的添加SSH key界面的步骤如下：

登录github 点击右上方的Accounting，再点击settings图标 选择 SSH and GPGkeys， 点击 New SSH key 在出现的界面中填写SSH key的名称，填一个你自己喜欢的名称即可 然后将上面拷贝的cat ~/.ssh/id_rsa.pub 出现的内容，粘贴到key一栏，在点击“Add SSH key”按钮就可以了。 添加过程github会提示你输入一次你的github密码 添加完成后再次执行git clone就可以成功克隆github上的代码库了。
```
### 2. windows：
安装视频和文件已经上传群共享。

