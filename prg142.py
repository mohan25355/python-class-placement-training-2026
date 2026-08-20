import os
if os.path.isfile("source.txt"):
    print("file is present")
    f=open("source.txt","r")
    result=f.read()
    print(result)
else:
    print("file is not present")