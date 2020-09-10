m=int(input())
M=set(map(int,input().split()))
n=int(input())
N=set(map(int,input().split()))
a=M.difference(N)
b=N.difference(M)
c=a.union(b)
d=list(c)
t=[]
for i in range(len(d)):
    j=i+1
    for j in range(len(d)):
        if d[i]<d[j]:
            t=d[i]
            d[i]=d[j]
            d[j]=t
for a in range(len(d)):
    print(d[a])
