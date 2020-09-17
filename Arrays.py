import numpy

def arrays(arr):
    reverse=arr[::-1]
    return numpy.array(reverse,float)
arr = input().strip().split(' ')
result = arrays(arr)
print(result)
