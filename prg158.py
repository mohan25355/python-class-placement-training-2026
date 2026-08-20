#friendly number
n=int(input("Enter a number 1: "))
a=int(input("Enter a number 2: "))
arr=[]
arr2=[]
sum=0
add=0
for i in range(1,n+1):
    if n%i==0 and i!=n:
        arr.append(i)
for j in range(len(arr)):
   sum=sum+arr[j]

for i in range(1,a+1):
    if a%i==0 and i!=a:
        arr2.append(i)
for j in range(len(arr2)):
   add=add+arr2[j]  
total=sum+add
t2=n+a
if total==t2:
    print("Friendly Pair")
else:
    print("Not a Friendly Pair")

print("sum of factor:" ,total)
print("sum of inputs:" ,t2)