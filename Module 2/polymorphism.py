# ================================
# POLYMORPHISM IMPLEMENTATION
# ================================

# Parent Class
class Animal:

    def sound(self):
        print("Animals make different sounds.")


# Child Class 1
class Dog(Animal):

    def sound(self):
        print("Dog says: Woof! Woof!")


# Child Class 2
class Cat(Animal):

    def sound(self):
        print("Cat says: Meow! Meow!")


# Child Class 3
class Cow(Animal):

    def sound(self):
        print("Cow says: Moo! Moo!")


# Create objects
dog = Dog()
cat = Cat()
cow = Cow()

# Demonstrate Polymorphism
animals = [dog, cat, cow]

print("Animal Sounds")
print("----------------")

for animal in animals:
    animal.sound()
