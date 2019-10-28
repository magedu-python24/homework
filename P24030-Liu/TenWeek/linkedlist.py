class Node:
    def __init__(self,node=None,value=None):
        self.value=value
        self.pRight=None
        self.pLeft=node
        if node!=None:
            node.pRight=self

class LinkedList:
    def __init__(self):
        self.pHead=Node()
        self.pLast=self.pHead
        self.len=0
    def __getnode__(self, index):
        if self.len > index and -self.len <= index:
            if index==self.len-1:
                return self.pLast
            if  index<0:
                index+=self.len
            if self.len//2 > index:
                node = self.pHead
                while index>=0:
                    node=node.pRight
                    index-=1
            else:
                node = self.pLast
                while index<self.len-1:
                    node=node.pLeft
                    index+=1
            return node
        else:
            raise IndexError('list index out of range');
    def __getitem__(self, key):
        return self.__getnode__(key).value

    def __setitem__(self, key, value):
        self.__getnode__(key).value=value

    def pop(self):
        if(self.pHead!=self.pLast):
            self.pLast=self.pLast.pLeft
            self.pLast.pRight=None
            self.len-=1
    def append(self,value):
        self.pLast=Node(self.pLast,value)
        self.len+=1
    def iternodes(self,reverse=False):
        if reverse:
            node=self.pLast
            while node.pLeft!=None:
                yield node.value
                node=node.pLeft
        else:
            node=self.pHead.pRight
            while node!=None:
                yield node.value
                node=node.pRight
    __iter__ = iternodes

    def remove(self,index:int):
        node=self.__getnode__(index)
        if node == None:
            print('error')
            return
        elif node==self.pLast:
            self.pop()
        else:
            pRight=node.pRight.pRight
            node.pRight=pRight
            pRight.pLeft=node
        self.len-=1

    def insert(self,index:int,value):
        node=self.__getnode__(index).pLeft
        if node == None:
            print('error')
            return
        elif node==self.pLast:
            self.append(value)
        else:
            pRight=node.pRight
            newNode=Node(node,value)
            newNode.pRight=pRight
            pRight.pLeft=newNode
        self.len+=1



l=LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
print(l[1])
print(l[-2])
l.insert(3,100)
l[4]=0
print('~~~~~~~~~~~~~~~')
print()
for i in l:
    print(i)
print('~~~~~~~~~~~~~~~')
for i in l.iternodes(reverse=True):
    print(i)

