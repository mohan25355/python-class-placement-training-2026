try:
    n=int(input("Enter a number: "))
    print(x)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except NameError:
        print("Variable not defined.")