num=int(input("enter a num: "))
temp=num
sum=0
if num>=1:
    print("natural number")
    for i in range(1,temp+1):
        sum=sum+i
    print(sum)
else:
    print("it is not an natural number")