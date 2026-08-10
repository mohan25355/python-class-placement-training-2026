num=int(input("enter a number"))
if(num<=1):
    print("the entered num is not prime")
else:
    flag=True
    for i in range(2,num):
        if(num%i==0):
            flag=False
            break
    if(flag):
            print("prime number")
    else:
            print("not prime")