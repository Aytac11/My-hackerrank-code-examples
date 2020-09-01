n=int(input())

for i in range(n):
    s=input().split(" ")
    try:
        l=int(s[0])//int(s[1])
        print(l)
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as c:
        print("Error Code:",c)
