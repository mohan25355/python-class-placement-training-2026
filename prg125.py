#with argument with return value
def swap(a,b):
    print("before swapping:",a,b)
    a,b=b,a
    return a,b
c=int(input("Enter a number 1: "))
d=int(input("Enter a number 2: "))
result=swap(c,d)
print("after swapping:",result)
