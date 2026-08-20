class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def celebrate_birthday(self):
        self.age+=1
        print(f"Happy Birthday {self.name}! You are now {self.age} years old.") 
name=input("Enter your name: ")
age=int(input("Enter your age: "))
p1=person(name, age)
p1.celebrate_birthday()
# p2=person("sai", 30)
# p2.celebrate_birthday()