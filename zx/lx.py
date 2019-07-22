num=int(input("-->"))
if num%2==0:
    num+=1
else:
    pass
row=int((num-1)/2)
for i in range(1,num+1):
    if i==1:
        print(" "*(row+1-i)+"*")
    elif i>1 and i<=row+1:
        print(" "*(row+1-i)+"*"*(i*2-1))
    else:
        print(" "*(i-row-1)+"*"*(num-2*(i-row-1)))

