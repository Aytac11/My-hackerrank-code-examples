import numpy
N,M=map(int, input().split())
numpy.set_printoptions(legacy='1.13')
arr=numpy.array([input().split(" ") for _ in range(N)],int)
print(numpy.mean(arr,  axis = 1))
print(numpy.var(arr,  axis = 0))
print(numpy.std(arr, axis = None))