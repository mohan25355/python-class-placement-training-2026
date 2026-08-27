#prime number range
series=input("enter a range: ")
n=series
for i in range(1,int(n)+1):
    arr=[]
    flag=0
    if int(series)>1:
        for j in range(1,int(i)+1):
            if int(i)%j==0:
                arr.append(j)
        for i in arr:
            if len(arr)==2:
                if i==1 or i==int(i):
                    flag=flag+1
        if flag==2:
            print(i,"is a prime number")