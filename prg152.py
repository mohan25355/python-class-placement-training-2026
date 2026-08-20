class person:
    def __init__(self,name,age,city,country):
        self.name=name
        self.age=age
        self.city=city
        self.country=country
        print(f"your name is {name} ,{age} years old live in {city} at {country}")
name=input("enter your name:")
age=int(input("enter your age: "))
city=input("enter your city: ")
country=input("enter your country: ")
person(name,age,city,country)