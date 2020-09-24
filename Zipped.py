n,m =map(int, input().split())
l=[]
for i in range(m):
    elem=map(float,input().split())
    l.append(elem)

for i in zip(*l):
    avrg=sum(i)/len(i)
    print(avrg)
