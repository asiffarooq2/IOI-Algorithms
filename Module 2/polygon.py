# ================================
# POLYGON AREA CALCULATOR
# ================================

class Polygon:

    # Constructor
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to calculate area
    def area(self):
        return self.length * self.width

    # Method to display details
    def display(self):
        print("\nPolygon Details")
        print("----------------------")
        print("Length :", self.length)
        print("Width  :", self.width)
        print("Area   :", self.area())


# Create an object
shape = Polygon(12, 8)

# Display details
shape.display()
