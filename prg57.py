num=int(input("enter num: "))
s=num
n=0
for i in range(1,num+1):
    print(" "*n+s*"*")
    n=n+1
    s=s-1