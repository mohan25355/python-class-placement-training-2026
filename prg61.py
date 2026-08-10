num=int(input("enter num: "))
a=num
b=num-2
flag=0
for i in range(1,num+1):
    print("*"*a)
    flag=flag+1
    for j in range(b+1):
        if(flag==2):
            break
        print("*"*1+" "*b+"*"*1)
    if(flag==2):
        break
    