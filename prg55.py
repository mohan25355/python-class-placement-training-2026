num=int(input("enter num: "))
for i in range(1,num+1):
    for j in range(i):
        print("*",end="\t")
    print()