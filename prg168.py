#prime number
num=input("enter a number:")
n=num
arr=[]
flag=0
if int(n)>1:
    for i in range(1,int(n)+1):
        if int(n)%i==0:
            arr.append(i)
for i in arr:
    if len(arr)==2:
        if i==1 or i==int(n):
            flag=flag+1
print(arr)
if flag==2:
    print("prime number")
else:
    print("not an prime number")