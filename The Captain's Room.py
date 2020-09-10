n=int(input())
l=list(map(int, input().split()))
s=set(l)
for i in s:
    l.remove(i)
    if i not in l:
        print(i)
        break
    
