row=int(input("Enter number of row: "))
letter=65
for i in range(1,row+1):
    for j in range(i):
        print(chr(letter),end="\t")
    print()
    letter+=1