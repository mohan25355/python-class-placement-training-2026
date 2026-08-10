num=int(input("enter a num: "))
fact=1
if num==0 and num==1:
    print(f"factorial{num} is 1")
elif num<0:
    print("no negative factorial ")
else:
    for i in range(1,num+1):
        fact=fact*i
    print(f"the factorial of {num} is {fact}")
