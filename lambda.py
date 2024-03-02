# one liner functions in python
def subtract(a, b):
    return a - b


def a_first(a):
    return a[1]


a = [[1.3], [2, 4], [4, 6]]
a.sort(key=a_first)
print()