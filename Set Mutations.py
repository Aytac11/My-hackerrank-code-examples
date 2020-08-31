n = int(input())
st1 = set(map(int, input().split()))
m = int(input())

for i in range(m):
    com, n = input().split()
    st2 = set(map(int, input().split()))
    if(com == "intersection_update"):
        st1.intersection_update(st2)
    elif(com == "update"):
        st1.update(st2)
    elif(com == "symmetric_difference_update"):
        st1.symmetric_difference_update(st2)
    elif(com == "difference_update"):
        st1.difference_update(st2)

print(sum(st1))
