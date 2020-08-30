import numpy


p=list(map(float,input().split()))
n=input()

print(numpy.polyval(p,int(n)))
