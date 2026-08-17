num=input("Enter a num: ")
sum=0
for i in num:
    fact = 1
    for j in range(1,(int(i))+1):
        fact = fact * j
    sum = sum + fact
print(sum)
if sum == int(num):
    print("Strong Number")  
else:
    print("Not a Strong Number")