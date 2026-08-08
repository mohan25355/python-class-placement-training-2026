n=int(input("eneter a num"))
for i in range(n):
    if(n>=10):
        break
    else:
        print(i)
else:   #default exectution statement
    print("finally")