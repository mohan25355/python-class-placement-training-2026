numbers=int(input("enter needed numbers: "))
action=input("+ or - or * or %: ")
sum=0
sub=0
mul=1
div=0
container=[]
length=len(str(container))
for i in range(1,numbers+1):
    num=int(input(f"Enter number{i}: "))
    container.append(num)
if action== "+":
    for i in range(length+1):
        sum=sum+container[i]
    print(f"the sum of {container} values are {sum}")
elif action=="-":
    for i in range(0,length):
        sub=container[i]-sub
    print(f"the sum of {container} values are {sub}")
elif action=="*":
    for i in range(length+1):
        mul=mul*container[i]
    print(f"the sum of {container} values are {mul}")
elif action=="%":
    for i in range(length):
        div=div%container[i]
    print(f"the sum of {container} values are {div}")
else:
    print("invalid input")




    
