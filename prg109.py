def add(a):
    b=a
    sum=0
    for i in b:
        sum=sum+i
    return sum
time=int(input("enter times: "))
tup=()
for i in range(time):
    n=int(input(f"enter num{i}: "))
    tup=tup+(n,)
print(tup)
result=add(tup)
print(result)