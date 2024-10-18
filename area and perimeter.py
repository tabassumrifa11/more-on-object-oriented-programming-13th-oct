

class Circle:
    
    def __init__(self, r):
        self.radius = r  

    def area(self):
        return 3.14 * self.radius ** 2  
    
    def perimeter(self):
        return 2 * 3.14 * self.radius 
    


radius = float(input("Enter the radius: "))


c1 = Circle(radius)

print(f"Area of the circle = {c1.area()}")
print(f"Perimeter of the circle = {c1.perimeter()}")  
