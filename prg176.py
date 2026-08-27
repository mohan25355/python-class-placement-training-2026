num = int(input("enter a num: "))
arr = []
for i in range(1, num + 1):
    if num % i == 0:
        arr.append(i)
print("the number of divisors are",len(arr))