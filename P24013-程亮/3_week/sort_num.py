#！/bin/env python3

num=[3, 5, 1, 7, 9, 6, 8]
nums=len(num)
for i in range(nums):
	flag=False
	for j in range(nums-i-1):
		if num[j] > num[j+1]:
			tmp=num[j]
			num[j]=num[j+1]
			num[j+1]=tmp
			flag=True
	if not flag:
		break
print(num)