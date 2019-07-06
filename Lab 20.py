#Class
#Jacob Norenberg
#July 3, 2019

class Circle:
    def __init__(self):
        self.radius = input("Enter radius: ")

    def calcArea(self):
        return 3.14*(int(self.radius)*int(self.radius))

circle1 = Circle()
circle2 = Circle()
print("Circle 1 Radius: ", circle1.radius)
print("Circle 1 Area: ", circle1.calcArea())
print("Circle 2 Radius: ", circle2.radius)
print("Circle 2 Area: ", circle2.calcArea())
