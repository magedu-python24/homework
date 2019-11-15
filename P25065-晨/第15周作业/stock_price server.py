import socket
import logging
import threading
import random
import time
import numpy as np

random.random()


logging.basicConfig(level=logging.INFO, format='%(asctime)s   %(message)s')

class Server:
    def __init__(self,ip='127.0.0.1',port=9999):
        self.addr = (ip,port)
        self.socket = socket.socket()
        #self.event = threading.Event()
        self.clients = {}

    def start(self):
        self.socket.bind(self.addr)
        self.socket.listen()
        threading.Thread(target=self.accept).start()

    def accept(self):
        while True:
            sock,client = self.socket.accept()
            self.clients[client] = sock
            logging.info(client)
            threading.Thread(target=self.stock_price).start()
            threading.Thread(target=self.recv,args=(sock,client)).start()

    def stock_price(self,p0=100):
        while True:
            p1 = p0 + np.random.standard_normal()
            time.sleep(2)
            for s in self.clients.values():
                s.send('Stock price is  {:.2f}'.format(p1).encode())
            p0 = p1

    def recv(self,socket,client):
        while True:
            data = socket.recv(1024)
            if data == b'quit':
                self.clients.pop(client)
                socket.close()
                break
            logging.info(data)


    def close(self):
        self.socket.close()

server = Server()
server.start()

print(threading.enumerate())

#server.close()