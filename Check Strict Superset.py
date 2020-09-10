A=set(map(int,input().split()))
n=int(input())

for i in range(n):
    sets=set(map(int,input().split()))
    if A.issuperset(sets)==False:
        print(False)
        break
    else:
        pass
else:
    print(True)
