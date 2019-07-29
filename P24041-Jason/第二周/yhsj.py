import copy
length=int(input("-->"))
ls_out=list()
ls_in=list()
for i in range(length):
    ls_out.append(ls_in)
    for j in range(i+1):
        if i==j:
            ls_in.append(1)
    for j in range(i):
        if i>1 and j>0:
            lc=copy.deepcopy(ls_out)
            ls_out=lc
            ls_out[i][j]=ls_out[i-1][j-1]+ls_out[i-1][j]
    print(ls_out[i])
