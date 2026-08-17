#strong number

n = input("Enter a number: ")
total = 0
for digit in n:
    fact = 1
    for i in range(1, int(digit) + 1):
        fact = fact * i
    total = total + fact
print(total)

if total == int(n):
    print("Strong Number")
else:
    print("Not a Strong Number")