import socket
import threading
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s  %(message)s')

class client:

    def __init__(self,ip='127.0.0.1',port=9999):
        self.client = socket.socket()
        self.raddr = (ip,port)
        self.client.connect(self.raddr)

    def start(self):
        threading.Thread(target=self.recv).start()

    def send(self,msg):
        self.client.send(msg.encode())

    def recv(self):
        while True:
            data = self.client.recv(1024)
            logging.info(data.decode())

    def stop(self):
        self.client.close()
if __name__ == "__main__":
    c = client()
    while True:
        msg = input('>>>')
        c.start()
        c.send(msg)

