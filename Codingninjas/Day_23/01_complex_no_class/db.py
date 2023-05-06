class ComplexNumbers:
    def __init__(self,real,img):
        self.real = real
        self.img = img 
    def Plus(self,obj):
        self.real = self.real + obj.real
        self.img = self.img + obj.img 
        self.Print()
    def Multiply(self,obj):
        a = self.real
        b = self.img
        c = obj.real
        d = obj.img
        self.real = (a * c) - (b * d)
        self.img = (a * d) + (b * c)
        self.Print()
    def Print(self):
        print("{0} + i{1}".format(self.real,self.img))
    #create your class here.
    
#Driver's code goes here.
r1 , i1 = map(int,input().split())
r2 , i2 = map(int,input().split())
operation = int(input())
obj1 = ComplexNumbers(r1,i1)
obj2 = ComplexNumbers(r2,i2)
if(operation==1):
    obj1.Plus(obj2)
elif(operation==2):
    obj1.Multiply(obj2)