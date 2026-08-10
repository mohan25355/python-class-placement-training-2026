num=int(input("enter a num: "))
b=num-1
a=1
c=1
d=num+2
for i in range(1,num+1):
    print(" "*b+"*"*a)
    b=b-1
    a=a+2
for j in range(1,num+1):
    print(" "*c+"*"*d)
    c=c+1
    d=d-2

   
        