n=int(input())
for i in range(n):
    numA=int(input())
    A=set(map(int,input().split()))
    numB=int(input())
    B=set(map(int,input().split()))
    subset=A.difference(B)
    if len(subset)==0:
        print("True")
    else:
        print("False")
