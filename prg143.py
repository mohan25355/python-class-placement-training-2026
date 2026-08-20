import os
if os.path.isfile("source.txt"):
    print("file is present")
    f=open("source.txt","r")
    result=f.read()
    print(result)
    os.remove("source.txt")
else:
    if os.path.isfile("source.txt"):
     print("file is present")
    else:
     print("file deleted sucessfully")