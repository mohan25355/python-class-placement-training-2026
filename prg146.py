#armstrong number
n=int(input("enter a num: "))
n1=len(str(n))
temp = n
sum=0
while temp>0:
    for i in range(n1):
        digit=temp%10
        sum+=digit**n1
        temp//=10
if sum==n:
    print("armstrong")
else:
    print("not armstrong")
