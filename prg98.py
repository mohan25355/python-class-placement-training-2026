n=int(input())
a=1
space=n-1
for i in range(1,n+1):
    print(" "*space+"*"*a)
    space-=1
    a+=2

