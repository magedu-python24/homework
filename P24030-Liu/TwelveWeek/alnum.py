from threading import Thread, Event
class Show:
    def __init__(self):
        self.eventA = Event()
        self.eventD = Event()

    def showAlpha(self):
        for i in range(65,91):
            self.eventA.wait()
            self.eventA.clear()
            print(chr(i))
            self.eventD.set()
        self.eventD.set()

    def showDigit(self):
        for i in range(1,27):
            print(i,end='')
            self.eventA.set()
            self.eventD.wait()
            self.eventD.clear()
        self.eventA.set()


s = Show()
if __name__ == '__main__':
    Thread(target=s.showAlpha, name='showAlpha').start()
    Thread(target=s.showDigit, name='showDigit').start()
