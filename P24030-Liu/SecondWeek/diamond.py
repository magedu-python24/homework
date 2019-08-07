#

len=7
n=len>>1
[print(' '*abs(i) + '*'*(len-abs(i)*2)) for i in range(-n,n+1)]
print()

[print(' '*(n-abs(i)) + '*'*(abs(i)*2+1)) for i in range(-n,n+1)]
print()

for i in range(-n,n+1):
    if i<0:
        print(' '*abs(i) + '*'*(4+i))
    elif i>0:
        print(' '*3 + '*'*(4-i))
    else:
        print('*'*len)
