age = int(input("Enter Your Age: "))
driving_license =input("you have driving license (yes/no)")
if(age>=18):
    if(driving_license == "yes" or driving_license == "Yes" or driving_license == "YES"):
        print("you can drive")
    elif(driving_license=="no" or driving_license=="No" or driving_license=="NO" ):
        print("you can't drive")
    else:
        print("invalid input")
else:
    print("you are too young to drive")