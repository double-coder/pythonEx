import numpy

a = list()

for _  in range(2):
    n = map(int, input())
    a.append(n)

print (numpy.outer(a[0], a[1]))
print (numpy.inner(a[0], a[1]))
