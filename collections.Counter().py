from collections import Counter

n=int(input())
lst=Counter(map(int,input().split()))
customers=int(input())
s=0
for i in range(customers):
    shoes_size,shoes_price=map(int,input().split())
    if lst[shoes_size]:
        s+=shoes_price
        lst[shoes_size]-=1
print(s)
