def count(n):
    if n<=0:
        print("done!")
    else:
        print(n)
        count(n-1)
count(5)