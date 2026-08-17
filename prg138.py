#perfect number
n=int(input("Enter a number: "))
arr=[]
sum=0
for i in range(1,n+1):
    if n%i==0 and i!=n:
        arr.append(i)
for j in range(len(arr)):
   sum=sum+arr[j]
if sum==n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")