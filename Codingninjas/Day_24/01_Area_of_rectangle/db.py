class Rectangle:
    def getArea(self):
        res = self.length * self.breadth 
        return res 
obj = Rectangle()
print(obj.getArea(5,10))