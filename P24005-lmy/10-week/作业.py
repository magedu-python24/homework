
class Ob:
    def __init__(self, name):
        self.name = name
        self.items = []

    def __add__(self, other):
        self.items.append(other)
        return self

    def __setitem__(self, key, value):
        self.items[key] = value

    def __mul__(self, n):
        self.items = self.items * n

    def __len__(self):
        return len(self.items)

    def __delitem__(self, key):
        self.items.pop(key)

    def __hash__(self):
        return True

    def __eq__(self, other):
        return False

    def __repr__(self):
        return '{}'.format(self.items)

a = Ob('tom')
b = Ob('tom')
a + 1 + 2
print('a:', a)
a[0] = 'a'
print('a:', a)
a * 3
print('a:', a)
print('len:', len(a))
del a[1]
print('a: ', a)






# 执行以下操作：

print('set: ', {a, b})
# 其输出如下：

# a: ['a', 'a', '2', 'a', '2']
# set: { < Ob
# name = tom
# items = ['a', 'a', '2', 'a', '2'] >}