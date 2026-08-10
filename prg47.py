num=int(input("enter a num: "))
temp=num
length=len(str(num))
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**length
    temp//=10
result=sum
if(result==num):
    print("it is an armstrong number")
else:
    print("not an factorial")
