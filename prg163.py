class fact:
    def __init__(self,num):
        self.num=num
        self.arr=[]
        for i in range(1,self.num+1):
            self.num=i
            length=len(str(self.num))
            sum=0
            while self.num>0:
                digit=self.num%10
                sum=sum+(digit**length)
                self.num=self.num//10
            if sum==i:
                self.arr.append(i)
        print(self.arr)
input_value=int(input("enter a value: "))
fact(input_value)