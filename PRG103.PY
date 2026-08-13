def add(a):
    b=a
    sum=0
    for i in b:
        sum=sum+i
    return sum
n=map(int,input("enter num: ").split())
li=tuple(n)
print(li)
result=add(li)
print(result)