# ================================
# ANIMAL CLASS
# ================================

# Create a class
class Animal:

    # Constructor
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    # Method to display animal details
    def display(self):
        print("\nAnimal Details")
        print("----------------------")
        print("Name    :", self.name)
        print("Species :", self.species)
        print("Sound   :", self.sound)

    # Method to make the animal speak
    def speak(self):
        print(self.name, "says", self.sound)


# Create objects
animal1 = Animal("Leo", "Lion", "Roar")
animal2 = Animal("Daisy", "Cow", "Moo")

# Display details
animal1.display()
animal1.speak()

animal2.display()
animal2.speak()
