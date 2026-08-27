class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def data1(self):
        print("name: ",self.name)
        print("age: ",self.age)
class student2:
    def __init__(self,dept,sec,roll):
         self.dept=dept
         self.sec=sec
         self.roll=roll
    def data2(self):
        print("Dept:",self.dept)
        print("Sec:",self.sec)
        print("Roll:",self.roll)
class show(student,student2):
    def __init__(self,name,age,dept,sec,roll,num ):
        self.num=num
    def show_data(self):
        p2=student
        p3=student2
        p2.data1()
        p3.data2()
        print("number: ",self.num)


# name=input("enter your name: ")
# age=int(input("enter your age: "))
# dept=input("enter dept: ")
# sec=input("enter your sec: ")
# roll=int(input("enter your roll number: "))
# num=int(input("enter number of students: "))
name="mohan"
age=20
dept="cse"
sec="c"
roll=421624104123
num=6382445409

p1=show(name,age,dept,sec,roll,num)
p1.show_data()