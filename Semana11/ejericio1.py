# 1. Cree una clase de `Circle` con:
#     1. Un atributo de `radius` (radio).
#     2. Un método de `get_area` que retorne su área.

import math

class Circle:
    
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        area = math.pi * self.radius**2
        print(f"Area: {round(area, 2)}")
        
new_circle = Circle(6)
new_circle.get_area()