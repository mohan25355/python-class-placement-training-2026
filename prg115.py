a=[1,2,3,4,5,6,7]
b=list(filter(lambda a:a%2!=0,a))
c=list(filter(lambda a:a%2==0,a))
print("odd: ",b)
print("even: ",c)