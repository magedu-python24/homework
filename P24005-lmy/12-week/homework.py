import threading

class Show:
    def __init__(self):
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()

    def show_number(self):
        for i in range(1, 27):
            self.lock1.acquire()
            print(i, end='')
            self.lock2.release()

    def show_alpha(self):
        for i in range(1, 27):
            self.lock2.acquire()
            print(chr(i+64))
            self.lock1.release()

a = Show()

if __name__ == '__main__':
    a.lock2.acquire()
    threading.Thread(target=a.show_number).start()
    threading.Thread(target=a.show_alpha).start()

