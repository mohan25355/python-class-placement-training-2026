student=[("mohan",20),("hari",80),("sreeram",30),("ram",29)]
fruit=["apple","pir","mango","banana","grapes"]
sort_student=sorted(student,key=lambda x :x[1])
sort_fruit=sorted(fruit,key=lambda x :len(x))
print(sort_student)
print(sort_fruit)