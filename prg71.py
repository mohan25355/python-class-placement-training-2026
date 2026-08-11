text=input("Enter a text to check wheather it is an palimdrom: ")
a=text[::-1]
print(a)
if text==a:
    print("it is palindrom")
else:
    print("it is not a palindrom")