x=1
y=1
sum=0
count=2
while 1:
    sum=x+y
    count+=1
    x=y
    y=sum
    if count==101:
        print(sum)
