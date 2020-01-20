#### 名字解释：MAC地址、IP地址、TCP、UDP

MAC地址：英文名称（Media Access Control Address），俗称物理地址，长度为48位，12个16进制数，如00-16-EA-AE-3C-40。其前6位为网络硬件制造商编号（由IEEE分配），后6位是此厂商的系列产品编号，所以MAC地址在全世界来说，都是唯一的。

IP地址：英文名称（Internet Protocol），位于TCP/IP模型的网络层，用来标记网络上的设备用的，具有唯一性，由网络地址和主机地址组成。

TCP:英文名称（Transmission Control Protocol），中文名为传输控制协议，位于TCP/IP协议中的传输层，应用层向TCP传输层发送用于网间传输的、用8位字节表示的数据流，然后TCP把数据流分区成适当长度的报文段。之后TCP把结果包传给IP层，由它来通过网络将包传送给接收端实体的TCP层。TCP为了保证不发生丢包，就给每个包一个序号，同时序号也保证了传送到接收端实体的包的按序接收。然后接收端实体对已成功收到的包发回一个相应的确认（ACK）；如果发送端实体在合理的往返时延（RTT）内未收到确认，那么对应的数据包就被假设为已丢失将会被进行重传。TCP用一个校验和函数来检验数据是否有错误；在发送和接收时都要计算校验和。

UDP: 英文名称（User Datagram Protocol），中文名为用户数据报协议，位于TCP/IP协议中的传输层。UDP协议与TCP协议一样用于处理数据包，UDP有不提供数据包分组、组装和不能对数据包进行排序的缺点，也就是说，当报文发送之后，是无法得知其是否安全完整到达的，但是效率极高，适用于要求传输效率，但不要求传输完整性的场景，如视频会议，NFS, DNS等。

#### 阐述如有一主机A向主机B发送数据包在网络上经过的各个步骤

A主机将数据打包（应用层）发送给传送层（TCP）注明源端口和目标端口，然后再传给网络层（IP）注明源地址和目标地址，此时再发送给数据链接层，形成一个完整的数据包，发送给路由器。此时路由器会在目的地地址之间选择最近的路由进行传输，B主机接收到数据包后，由数据链路层，网络层，传输层，应用层层层解析，最后得到数据包内的数据。

#### 自己安装nginx纪录安装文档，并写一份反向代理的配置文件

OS：centos 7 (x86_64位)

1、在/etc/yum.repos.d/下建立nginx.repo文件，内容如下：

```shell
[nginx-stable]
name=nginx stable repo
baseurl=http://nginx.org/packages/centos/$releasever/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://nginx.org/keys/nginx_signing.key
module_hotfixes=true

[nginx-mainline]
name=nginx mainline repo
baseurl=http://nginx.org/packages/mainline/centos/$releasever/$basearch/
gpgcheck=1
enabled=0
gpgkey=https://nginx.org/keys/nginx_signing.key
module_hotfixes=true
```



2、执行yum install nginx安装nginx, 启动nginx，配置反向代理

```shell
# 安装nginx
yum install nginx

# 启动nginx
systemctl start nginx

# 开机自启
systemctl enable nginx

# 配置反向代理，在/etc/nginx/conf.d下新建proxy.conf,内容如下：
# 先移除其它以配置文件，以免冲突： rm -rf /etc/nginx/conf.d/*.conf
server {
    listen       80;
    server_name  localhost;

    location / {
        proxy_pass   http://127.0.0.1:6666;
    }

}

# 根据需要，可以为proxy配置其它内容，参见http://nginx.org/en/docs/http/ngx_http_proxy_module.html

```

至此反向代理配置完成

