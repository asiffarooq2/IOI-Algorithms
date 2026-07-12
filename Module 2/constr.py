# ================================
# CONSTRUCTOR AND DESTRUCTOR
# ROBOT CLASS
# ================================

class Robot:

    # Constructor
    def __init__(self, name):
        self.name = name
        print("Constructor Called")
        print("Robot", self.name, "has been created.")

    # Method
    def introduce(self):
        print("Hello! I am", self.name)

    # Destructor
    def __del__(self):
        print("Destructor Called")
        print("Robot", self.name, "has been destroyed.")


# Create an object
robot1 = Robot("RoboX")

# Call a method
robot1.introduce()

# Delete the object
del robot1

print("Program Ended")
