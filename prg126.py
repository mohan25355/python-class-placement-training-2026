#with argument without return value
def swap(a,b):
    print("before swapping:",a,b)
    a,b=b,a
    print("after swapping:",a,b)

c=int(input("Enter a number 1: "))
d=int(input("Enter a number 2: "))
swap(c,d)
#step1:start
#step2:input from user
#step3:call swap function
#step4:print before swapping
#step5:swap values a=b,b=a
#step6:print after swapping
#step7:stop