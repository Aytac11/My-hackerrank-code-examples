from collections import Counter
l=list()
for i in range(int(input())):
    l.append(input())
print(len(Counter(l)))
for j in Counter(l).values():
    print(j, end=" ")
