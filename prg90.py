student_data={
        "student_name": "",
        "dept":"",
        "college" : "Mailam Engineering College",  
        "year": 2,
        "result": "fail"
}

#collection of data
student_data["student_name"]=input("enter name: ")
student_data["dept"]=input("enter dept: ")
student_data["college"]=input("enter college name: ")
student_data["year"]=input("enter year of studing: ")
student_data["result"]=input("enter result: ")
print("\n")

#print output
print("Name:",student_data["student_name"])
print("Dept:",student_data["dept"])
print("College:",student_data["college"])
print("Year:",student_data["year"],"year")
print("Result:",student_data["result"])
print("\n")

#modify
student_data["result"]= " pass"

#modified result
print("Name:",student_data["student_name"])
print("Dept:",student_data["dept"])
print("College:",student_data["college"])
print("Year:",student_data["year"],"year")
print("Result:",student_data["result"])