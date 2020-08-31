from itertools import combinations_with_replacement

s,n=input().split()

a=combinations_with_replacement(sorted(s),int(n))
for i in a:
    print("".join(i))
