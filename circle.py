import math

class Circle:
    """A class to represent a circle and calculate its properties."""
    
    def __init__(self, radius):
        """Initialize a Circle object with a given radius."""
        self.radius = float(radius)
    
    def calculate_perimeter(self):
        """Calculate the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius
    
    def calculate_area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2