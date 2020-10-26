def print_rangoli(n):

    alp=[]
    for num in range(97,123):
        alp.append(chr(num))
    middleStr=alp[n-1::-1]+alp[1:n]
    signStr="-".join(middleStr)
    length=len(signStr)

    for integer in range(1,n):
        print("-".join(alp[n-1:n-integer:-1]+ alp[n-integer:n]).center(length,"-"))

    for integer in range(n,0,-1):
        print("-".join(alp[n-1: n-integer: -1] + alp[n-integer:n]).center(length,"-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
