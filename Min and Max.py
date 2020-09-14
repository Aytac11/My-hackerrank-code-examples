import numpy
N,M=map(int, input().split())

arr=numpy.array([input().split() for _ in range(N)],int)
p=numpy.min(arr, axis = 1)
d=numpy.max(p, axis=0)
print(d)
