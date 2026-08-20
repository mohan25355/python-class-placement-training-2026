try:
    n=input("enter your points: ")
    if int(n)>=100:
        print("level two ku ready ya!!!!!!")
except NameError:
        print("need more points")
except TypeError:
     print("wrong input")
else:
    print("you are ready for level two ku!!!!!!")