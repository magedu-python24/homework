
def logger(fn):
    import datetime
    import functools
    @functools.wraps(fn)
    def wrapper(*args,**kwargs):
        start=datetime.datetime.now()
        ret=fn(*args,**kwargs)
        delta=(datetime.datetime.now()-start)
        return  ret 
    return wrapper

@logger
def sort(arr:list,fn='insert'):
    length=len(arr)
    def insert():
        for j in range(2,length):
            key=arr[j]
            i=j-1
            while arr[i] > key and i >=0:
                arr[i+1]=arr[i]
                i-=1
            arr[i+1]=key

    def merge(left,right,tmp=[0]*length):
        if left<right:
            mid=(left+right)>>1
            merge(left,mid)
            merge(mid+1,right)
            i=left
            j=mid+1
            k=0
            while i<=mid and j<=right:
                if arr[i] < arr[j]:
                    tmp[k]=arr[i]
                    i+=1
                else:
                    tmp[k]=arr[j]
                    j+=1
                k+=1
            while i<=mid:
                tmp[k]=arr[i]
                k+=1
                i+=1
            while j<=right:
                tmp[k]=arr[j]
                k+=1
                j+=1
            for i in range(k):
                arr[left+i]=tmp[i]

    def quick(left,right):
        if left<right:
            i=left
            j=right
            k=arr[left]
            while i<j:
                while arr[j]>k:
                    j-=1
                arr[i]=arr[j]
                i+=1
                while i<j and arr[i]<k:
                    i+=1
                arr[j]=arr[i]
                j-=1
            arr[i]=k
            quick(left,i-1)
            quick(j+1,right)
    def heapcreate1(k=1):
        t=k<<1
        if t<<1 <= length:
            heapcreate1(t+1)
            heapcreate1(t)

        if t<=length:
            i=t if t==length or arr[t]>arr[t+1] else t+1
            if arr[k]<arr[i]:
                arr[k],arr[i]=arr[i],arr[k]

        if t<<1 <= length:
            heapcreate1(t+1)
            heapcreate1(t)
    def heapcreate2():
        for i in range(length>>1,0,-1):
            k=i
            while k<<1 <= length:
                t=k<<1
                j=t if t==length or arr[t]>arr[t+1] else t+1
                if arr[k]<arr[j]:
                    arr[k],arr[j]=arr[j],arr[k]
                    k=j
                else:
                    break
    def heap():
        for i in range(length,1, -1):
            arr[1],arr[i]=arr[i],arr[1]
            k=1
            while k<<1 < i:
                t=k<<1
                j=t if t==i-1 or arr[t]>arr[t+1] else t+1
                if arr[k]<arr[j]:
                    arr[k],arr[j]=arr[j],arr[k]
                    k=j
                else:
                    break

    if fn=='insert':
        insert()
    elif fn=='merge':
        merge(0,length-1)
    elif fn=='quick':
        quick(0,length-1)
    elif fn=='heap':
        length-=1
        heapcreate2();
        heap();
    else:
        print('fn unknown')


import random
#arr=[random.randint(0,100000) for i in range(10000)]
#sort(arr,'insert')
arr=[random.randint(0,100000) for i in range(1000000)]
sort(arr,'merge')
arr=[random.randint(0,100000) for i in range(1000000)]
sort(arr,'quick')
arr=[random.randint(0,100000) for i in range(1000000)]
sort(arr,'heap')
#print(arr)

