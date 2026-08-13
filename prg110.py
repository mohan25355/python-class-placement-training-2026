def welcome(*match):#arbitary argument
    print("the len of the score is: ",len(match))
    for i in match:
        print("score: ",i)

welcome(10,2,5,9,6,3,9,10,2,5)