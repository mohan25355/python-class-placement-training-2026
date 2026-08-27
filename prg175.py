#factores
num=int(input("enter a num: "))
n=num
arr=[]
for i in range(1,int(n)+1):
    if n%i==0:
        arr.append(i)
print(arr)
        