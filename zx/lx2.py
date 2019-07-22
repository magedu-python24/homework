num=int(input("请输入一个奇数"))
for i in range(num,-num-2,-2):
    if i>0:
        print(" "*int((i-1)/2),"*"*(num-i+1))
    else:
        print(" "*int(abs((i-1)/2)),"*"*(num-2*int(abs(i-1)/2)))
