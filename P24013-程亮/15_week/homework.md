#### 利用本周学习的知识实现如下效果的程序：

1. server端监听指定的tcp端口
2. server端预先实现简单加减法的代码(可以自行扩展其他更复杂功能)
3. client端可以通过socket连接与server端通信传输需要参数
4. server端根据传的参数计算结果并返回
5. client端打印返回结果 



```python
# server
import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        result = self.data.decode()
        if result[1] == '+':
            result = int(result[0]) + int(result[2])
        elif result[1] == '-':
            result = int(result[0]) - int(result[2])
        elif result[1] == '*':
            result = int(result[0]) * int(result[2])
        else:
            result = int(result[0]) / int(result[2])
        print("get input from {}:".format(self.client_address[0]))
        print(self.data.decode())
        self.request.sendall(str(result).encode().upper())


if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()

# client
import socket

HOST, PORT = "127.0.0.1", 9999
data = input("input like '1+2', '5*6' and so on: ")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))
    received = str(sock.recv(1024), "utf-8")
print("result from server side: {}".format(received))

```

