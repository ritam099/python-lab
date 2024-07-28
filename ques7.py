class Traingle :
    def __init__(self, side1, side2, side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3
        
    def area(self):
        semiPerimeter = (self.side1+self.side2+self.side3)/2
        area = (semiPerimeter*(semiPerimeter-self.side1)*(semiPerimeter-self.side2)*(semiPerimeter-self.side3))**0.5
        return area
    

sideA=int(input("enter length in cm of side A in triangle 1 : "))
sideB=int(input("enter length in cm of side B in triangle 1 : "))
sideC=int(input("enter length in cm of side C in triangle 1 : "))

obj1 = Traingle(sideA,sideB,sideC)
sideA=int(input("enter length in cm of side A in triangle 2 : "))
sideB=int(input("enter length in cm of side B in triangle 2 : "))
sideC=int(input("enter length in cm of side C in triangle 2 : "))

obj2 = Traingle(sideA,sideB,sideC)
area1 = obj1.area()
area2 = obj2.area()
totalArea = area1+area2

print("contribution of triangle 1 is ", (area1/totalArea)*100, "%")
print("contribution of triangle 2 is ", (area2/totalArea)*100, "%")