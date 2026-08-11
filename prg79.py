n=int(input("enter num: "))
student={}
for i in range(n):
    name=input(f"enter name{i+1}: ")
    mark=int(input(f"enter marks of {name}: "))
    student[name]=mark
print("dic: ",student)
print("marks: ",student[list(student.keys())[0]])
