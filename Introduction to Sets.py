def average(array):
   h=set(array)
   for i in range(len(h)):
       t=sum(h)/len(h)
   return t
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
