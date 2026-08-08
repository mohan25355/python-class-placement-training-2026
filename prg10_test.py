num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
num3 = int(input("Enter Number 3: "))

print("Biggest Number Amoug All is")

if(num1>=num2 and num1>=num3):
    print("Num1 is Biggest")
elif(num2>=num1 and num2>=num3):
    print("Num2 is Biggest")
else:
    print("Num3 is biggest")

print("Smallest Number Among All is")

if(num1<=num2 and num1<=num3):
    print("Num1 is Smallest")
elif(num2<=num1 and num2<=num3):
    print("Num2 is Smallest")
else:
    print("Num3 is Smallest")