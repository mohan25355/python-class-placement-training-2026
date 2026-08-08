i=1
password=int(input("enter your password to guess:"))
while i<9999:
    if(i==password):
        print(f"the password is found at {i} attempt")
        break
    i+=1