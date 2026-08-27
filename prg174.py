class parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def current(self):
        print("your name is", self.name)
        print("your current age is", self.age)


class child1(parent):
    def current(self):
        print(f"happy birthday {self.name}")
        self.age += 1
        print(f"your age is now {self.age}")

class child2(child1):
    def current(self):
        child1.current(self)
        if self.age >= 18:
            print(f"{self.name}, you are now eligible for voting")
        else:
            print(f"{self.name}, you are not eligible for voting")


a = child2("Mohan", 17)
a.current()


