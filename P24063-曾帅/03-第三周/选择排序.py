s = [3,2,1,11,9,6,8]
for i in range(7):
    tmp0=s[i]
    mi = i
    for j in range(i+1,7):
        if s[j] < tmp0:
            tmp0 = s[j]
            mi = j
    tmp1 = s[i]
    s[i] = tmp0
    s[mi] = tmp1
print(s)