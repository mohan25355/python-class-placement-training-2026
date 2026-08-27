class friend:
    def __init__(self,num1,num2):
        
    def friend1self.num1=num1
        self.num2=num2
        self.arr1=[]
        self.arr2=[]
        self.sum1=0
        self.sum2=0
        self.total=0(self):
        for i in range(1,self.num1):
            if self.num1%int(i)==0 and i!=self.num1:
                self.arr1.append(i)
        for j in range(len(self.arr1)):
             self.sum1=self.sum1+self.arr1[j]
        
    def friend2(self):
            for i in range(1,self.num2):
                if self.num2%int(i)==0 and i!=self.num2:
                    self.arr2.append(i)
            for j in range(len(self.arr2)):
                 self.sum2=self.sum2+self.arr2[j]
            
    def result(self):
         self.friend1()
         self.friend2()
         print("Factors of",self.num1,":",self.arr1)
         print("Factors of",self.num2,":",self.arr2)
         self.total=self.sum1+self.sum2
         print("sum of factor:" ,self.total)
         print("sum of inputs:" ,self.num1+self.num2)
         if self.total==self.num1+self.num2:
             return "Friendly Pair"
         else:
              return "Not a Friendly Pair"

    
n1=int(input("Enter a number 1: "))
n2=int(input("Enter a number 2: "))
p1=friend(n1,n2)
print(p1.result())