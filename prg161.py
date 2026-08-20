#armstrong number
num=int(input("Enter num: "))
n=num
length=len(str(num))
sum=0
while n>0:
    digit=n%10
    sum=sum+(digit**length)
    n=n//10
if sum==num:
    print(f"The given number {num} is armstrong number ")
else:
    print(f"The given number {num} is not armstrong number ")