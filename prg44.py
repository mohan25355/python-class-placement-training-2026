#maxof three numbers
a=int(input("enter num1: "))
b=int(input("enter num2 "))
c=int(input("enter num3: "))
if(a>b and a>c):
    print(f"{a} is greater number")
elif(b>a and b>c):
    print(f"{b} is greater number")
else:
    print(f"{c} is greater number")