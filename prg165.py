class harshad:
    def __init__(self,num):
        self.num=num
        sum=0
        for i in str(self.num):
            sum=sum+int(i)
        if self.num%sum==0:
            print("harshad number")
        else:
            print("not harshad number")
harshad(int(input("enter a number: ")))