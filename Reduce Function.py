from functools import reduce

marks = [75, 65, 180, 120, 60]
a = reduce(lambda x, y: x + y, marks)
print(a)


b = reduce(max,  [3, 9, 7, 5])
print(b)

c = reduce(lambda x, y: x == y, [1, 1, 1, 0])
print(c)
