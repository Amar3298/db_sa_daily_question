from sys import stdin
class Car:
    def __init__(self,noOfGear,color):
        self.noOfGearC = noOfGear
        self.colorC = color
    def printCarInfo(self):
        print("noOfGear: ",self.noOfGearC)
        print("color:", self.colorC)  
    #Write your constructor and printCarInfo method here.
        
        


class RaceCar(Car):
    def __init__(self,noOfGear,color,maxSpeed):
        super().__init__(noOfGear,color)
        self.maxSpeedC = maxSpeed
    def printInfo(self):
        super().printCarInfo()
        print("maxSpeed:",self.maxSpeedC)
    #Write your constructor and printRaceCarInfo method here.
      
#Driver's code

noOfGear = int(stdin.readline().rstrip())
color = stdin.readline().rstrip()
maxSpeed = int(stdin.readline().rstrip())
        
raceCar = RaceCar(noOfGear,color,maxSpeed)
raceCar.printInfo()