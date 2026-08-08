num = int(input("enter your number: "))
temp =num
n=len(str(temp))
sum = 0
while temp>0:
    digit=temp%10
    sum=sum+(digit**n)
    temp=temp//10
result=sum
print(result)
if(result==num):
    print("amstrong")
else:
    print("not amstrong")