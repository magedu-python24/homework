num=int(input("-->"))
for i in range(3,num):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
