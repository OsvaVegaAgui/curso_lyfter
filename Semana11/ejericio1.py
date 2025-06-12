# 1. Cree una clase de `Circle` con:
#     1. Un atributo de `radius` (radio).
#     2. Un método de `get_area` que retorne su área.

import math

class Circle:
    
    radius = 0
    
    def get_area(self):
        area = math.pi * self.radius**2
        print(f"Area: {round(area, 2)}")
        
new_circle = Circle()

new_circle.radius = int(input("Enter the radius of the circle: "))

new_circle.get_area()