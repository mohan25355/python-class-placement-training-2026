name = input("enter your name: ")
mobile_no = int(input("enter your mobile number: "))
annual_income = float(input("enter your annual salary: "))
age = int(input("enter your age: "))
ten = float(input("enter your 10th mark: "))
tw_mark = float(input("enter your 12th mark: "))

if(annual_income>=100000):
    if(ten>400 and tw_mark>=500):
        print("Eligible For admission")
    else:
        print("mark not enough")
else:
    print("not Eligible")