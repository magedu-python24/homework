ls=[3, 5, 1, 7, 9, 6, 8]
length=len(ls)
ls_sorted=[0]*length
for i in range(length):
    ls_sorted[i]=max(ls)
    ind=ls.index(max(ls))
    ls.remove(ls[ind])
print(ls_sorted)
