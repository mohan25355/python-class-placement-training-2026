#abundant number
n=int(input("enter a num: "))
arr=[]
sum=0
for i in range(1,n):
    if n%i==0:
        arr.append(i)
print(arr)
for i in arr:
    sum=sum+i
if sum>n:
    print("Abundant number")
else:
    print("not an abundant number")
    