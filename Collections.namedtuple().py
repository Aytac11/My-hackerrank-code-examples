from collections import namedtuple
n=int(input())
strs=input().split()
s=0
for i in range(n):
    tel=namedtuple("telebe",strs)
    str1,str2,str3,str4=input().split()
    telebe=tel(str1,str2,str3,str4)
    s+=int(telebe.MARKS)
    avrg=s/n
print(avrg)
