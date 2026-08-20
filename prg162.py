#armstrong number in series
series=int(input("Enter the series: "))
arr=[]
for i in range(1,series+1):
    num=i
    length=len(str(num))
    sum=0
    while num>0:
        digit=num%10
        sum=sum+(digit**length)
        num=num//10
    if sum==i:
        arr.append(i)
print(arr)
