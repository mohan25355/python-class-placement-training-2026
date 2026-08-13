def add(a):
    b=a
    sum=0
    for i in b:
        sum=sum+i
    return sum
time=int(input("enter times: "))
tup=[]
for i in range(time):
    n=int(input(f"enter num{i}: "))
    tup.append(n)
    li=tuple(tup)
print(li)
result=add(li)
print(result)