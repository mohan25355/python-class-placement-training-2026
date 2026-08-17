def inte(prompt):
    try:
        value=int(input(prompt))
        return value
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return inte(prompt)
inte(25)