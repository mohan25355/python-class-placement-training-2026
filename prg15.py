score = int(input("enter your score: "))
attendance=int(input("enter your attendance percentage: "))
submitted = input("are you submitted your attendance(yes/no): ")

if(score>=60):
    if(attendance>=80):
        if(submitted == "yes" or submitted == "Yes" or submitted == "YES"):
            print("you are passed with good attendance and also submitted your assignments ")
        elif(submitted == "no" or submitted == "No" or submitted == "NO"):
            print("you are passed with good attendance but not submitted your assignments")
        else:
            print("invalid input")
    else:
        print("you are passed but attendance is low")
else:
    print("your fail")
