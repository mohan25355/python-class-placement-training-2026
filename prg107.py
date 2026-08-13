def add(a):
    b=a
    sum=0
    for i in b:
        sum=sum+i
    return sum
n=tuple(map(int,input("enter num: ").split()))
print(n)
result=add(n)
print(result)