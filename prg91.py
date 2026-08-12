student=("MOhan",20,"CSE")
course={"mech","thermo","it"}
grades={
    "mech":90,
    "thermo":25,
    "it":69
    }
print(f"student name: {student[0]},Age:{student[1]},Course:{student[2]}")
print("course: ",course)
for sub,mark in grades.items():
    print(f"{sub}:{mark}")