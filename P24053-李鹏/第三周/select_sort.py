# 使用选择排序算法实现排序[3, 5, 1, 7, 9, 6, 8]
# collection = [3, 5, 2, 7, 2, 6, 8]
collection = [3, 5, 1, 7, 9, 6, 8]
length = len(collection)
for i in range(length - 1):
    least = i
    for k in range(i + 1, length):
        if collection[k] < collection[least]:
            least = k
        collection[least], collection[i] = collection[i], collection[least]
print(collection)