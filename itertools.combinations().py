from itertools import combinations
s,n=input().split()
for i in range(int(n)):
    l=list(combinations(sorted(s),i+1))
    for j in l:
        print(''.join(j))
        
