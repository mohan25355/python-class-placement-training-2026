n=int(input ("loop time: "))
fruit={"apple","orange","apple","mango"}
print(fruit)
for i in range (1,n+1):
    text=input("enter data: ")
    fruit.add(text)
print(fruit)
fruit.remove("orange")
print(fruit)