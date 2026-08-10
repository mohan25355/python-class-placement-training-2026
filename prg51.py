numbers=int(input("enter needed numbers: "))
# action=input("+ or - or * or %: ")
container=[]
length=len(str(container))
for i in range(1,numbers+1):
    num=int(input(f"Enter number{i}: "))
    container.append(num)
print(container)
print(length)
