#with out argument with out return value
def swap():
    a=int(input("Enter a number 1: "))
    b=int(input("Enter a number 2: "))
    print("before swapping:",a,b)
    a,b=b,a
    print("after swapping:",a,b)
swap()