import numpy
N,M=map(int, input().split())

arr=numpy.array([input().split() for _ in range(N)],int)
p=numpy.sum(arr, axis = 0)
d=numpy.prod(p, axis=0)
print(d)
