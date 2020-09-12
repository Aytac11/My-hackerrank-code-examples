n=int(input())
for i in range(n):
    s=input()
    if len(s)==10 and s[0] in "7,8,9" and s.isdigit():
        print("YES")
    else:
        print("NO")
