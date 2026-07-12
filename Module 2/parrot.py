# ================================
# PARROT BIRD CLASS
# ================================

# Create a class
class Parrot:

    # Constructor
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    # Method to display details
    def display(self):
        print("\nParrot Details")
        print("----------------")
        print("Name :", self.name)
        print("Color:", self.color)
        print("Age  :", self.age, "years")

    # Method to make the parrot speak
    def speak(self):
        print(self.name, "says: Hello! Hello!")


# Create objects
parrot1 = Parrot("Mithu", "Green", 2)
parrot2 = Parrot("Rio", "Blue", 3)

# Call methods
parrot1.display()
parrot1.speak()

parrot2.display()
parrot2.speak()
