#automorphic number
n=int(input("Enter num: "))
a=n**2
print(a)
if str(a).endswith(str(n)):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")