class person:
    def __init__(self,name,num):
        self.name=name
        self.num=num
    def show(self):
        print("Name:",self.name)
class employee(person):
    def show(self):
        print("Employee Name:",self.name)
        print("value:",self.num+5)
emp=employee("mohan",10)
print("name: ",emp.name)
emp.show()