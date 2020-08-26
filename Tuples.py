if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=()
    for i in range(n):
        t+=integer_list
    print(hash(t))
