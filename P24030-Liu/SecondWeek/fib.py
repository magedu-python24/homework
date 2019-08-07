#

a=0
b=1

i=2
length=101

while i<=length:
    c=a+b
    a=b
    b=c
    i+=1
print(c)
