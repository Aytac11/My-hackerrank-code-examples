from itertools import permutations
s,n = input().split(" ")
p = list(permutations(s, int(n)))
p.sort()

for i in p:
    print("".join(i))
