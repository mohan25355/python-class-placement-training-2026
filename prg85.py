set_a=input("enter set for a: ").split()
set_b=input("enter set for b: ").split()
a={int(num) for num in set_a}
b={int(num2) for num2 in set_b}

print("Union ",a | b)
print("Intersection: ", a & b)
print("Difference: ", a-b)