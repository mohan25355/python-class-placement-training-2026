num=input("enter a range:")
value=int(input("enter a value:"))
n=num
arr=[]
for i in range(1,int(n)+1):
    if int(i)%value==0:
        arr.append(i)
print(arr)
