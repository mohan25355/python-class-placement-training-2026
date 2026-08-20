class test:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print("hello,my name is "+self.name)
p1=test("mohan",20)
p1.greet()