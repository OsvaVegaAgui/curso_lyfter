# 2. Cree una clase abstracta de `Shape` que:
#     1. Tenga los métodos abstractos de `calculate_perimeter` y `calculate_area`.
#     2. Ahora cree las siguientes clases que hereden de `Shape` e implementen esos métodos: `Circle`, `Square` y `Rectangle`.
#     3. Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
	
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Square(Shape):
    
    def __init__(self, side):
        self.side = side
   
    def calculate_area(self):
        area = self.side * self.side
        print(f"The area of the square is: {area}")


    def calculate_perimeter(self):
        perimeter = self.side * 4
        print(f"The perimeter of the square is: {perimeter}")
        
class Rectangle(Shape):
    
    def __init__(self, length, width):
        self.length = 	length
        self.width = width
   
    def calculate_area(self):
        area = self.length * self.width
        print(f"The area of the rectangle is: {area}")

    def calculate_perimeter(self):
        perimeter = 2*(self.length + self.width)
        print(f"The perimeter of the rectangle is: {perimeter}")
        
class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius
   
    def calculate_area(self):
        area = math.pi * self.radius**2
        print(f"The area of the circle is: {round(area,2)}")


    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        print(f"The circumference of the circle is: {round(perimeter,2)}")    
        
square1 = Square(5)
square1.calculate_area()
square1.calculate_perimeter()

print("\n ********** \n")

rectangle = Rectangle(4,2)
rectangle.calculate_area()
rectangle.calculate_perimeter()

print("\n ********** \n")

circle1 = Circle(33)
circle1.calculate_area()
circle1.calculate_perimeter()
