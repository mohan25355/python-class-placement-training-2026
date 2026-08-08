def week(day):
    match day:
        case 1 :
            print("sunday")
        case 2 :
            print("monday")
        case 3 :
            print("tuesday")
        case 4 :
            print("wednesday")
        case 5 :
            print("thursday")
        case 6 :
            print("friday")
        case 7 :
            print("saturday")
        case _ :
            print("Invalid Input")
num=int(input("Enter a num(1-7) get the day in a week: "))
result = week(num)