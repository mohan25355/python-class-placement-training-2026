a=input("enter a text: ")
print(a.swapcase())
print(a.title())
print(a.capitalize())
print(a.upper())
print(a.lower())
print(a.islower())
print(a.isupper())
#searching and replacing string methodes
print(a.find("world"))
print(a.count(a))
print(a.startswith("hello"))
print(a.endswith("hellos"))
print(a.replace("hello","hi"))

#string whitespace

print(a.strip())
print(a.lstrip())
print(a.rstrip())

# join method

#we need to split the string then only we can join
a= "apple mango orange"
fruit=a.split(" ")
print(fruit)
print("-".join(fruit))