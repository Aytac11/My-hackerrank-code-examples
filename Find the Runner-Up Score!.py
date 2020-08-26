if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    max=arr[0]
    for i in arr:
        if max<i:
            max=i
    max=max-1
    while max not in arr:
        max=max-1
    print(max)
