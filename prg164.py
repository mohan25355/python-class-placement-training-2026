#harshad number
num=int(input("enter a number: "))
n=num
sum=0
if len(str(n))>=2:
    for i in str(n):
        sum=sum+int(i)
    if num%sum==0:
        print("harshad number")
    else:
        print("not harshad number")
else:
    print(f"the value {num} is single digit")