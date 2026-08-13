def details(**name):
    a=len(name)
    print("first name: "+name["fname"])
    for i in range(a-1):
        print(name)
details(fname="mohan",lname="sundaram")
details(fname="hari",lname="haran")
details(fname="mec")