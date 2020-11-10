from itertools import groupby
for i, x in groupby(input()):
    t=tuple([len(list(x)), int(i)])
    print(t, end=" ")
