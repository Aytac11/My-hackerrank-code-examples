import numpy
numpy.set_printoptions(sign=' ')
x,y=map(int,input().split())
print(numpy.eye(x,y,k=0))
