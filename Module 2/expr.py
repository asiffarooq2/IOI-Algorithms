# ================================
# EXPRESSION CLASS
# ================================

class Expression:

    # Constructor
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # Addition
    def add(self):
        print("Addition:", self.num1 + self.num2)

    # Subtraction
    def subtract(self):
        print("Subtraction:", self.num1 - self.num2)

    # Multiplication
    def multiply(self):
        print("Multiplication:", self.num1 * self.num2)

    # Division
    def divide(self):
        if self.num2 != 0:
            print("Division:", self.num1 / self.num2)
        else:
            print("Division by zero is not possible.")


# Create an object
exp = Expression(20, 5)

# Call methods
exp.add()
exp.subtract()
exp.multiply()
exp.divide()
