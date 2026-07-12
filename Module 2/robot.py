# ================================
# ROBOT INTRODUCTION
# ================================

# Create a class
class Robot:

    # Constructor
    def __init__(self, name, model, purpose):
        self.name = name
        self.model = model
        self.purpose = purpose

    # Method to introduce the robot
    def introduce(self):
        print("Hello! My name is", self.name)
        print("Model:", self.model)
        print("Purpose:", self.purpose)
        print("Nice to meet you!")


# Create objects
robot1 = Robot("RoboX", "RX-101", "Helping Students Learn Python")
robot2 = Robot("TechBot", "TB-202", "Assisting with Household Tasks")

# Call the method
robot1.introduce()

print()

robot2.introduce()
