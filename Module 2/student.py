# ================================
# STUDENT CLASS
# ================================

# Create a class
class Student:

    # Constructor
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    # Method to display student details
    def display(self):
        print("\nStudent Details")
        print("----------------")
        print("Name :", self.name)
        print("Age  :", self.age)
        print("Grade:", self.grade)


# Create objects
student1 = Student("Aarav", 14, "8th")
student2 = Student("Priya", 13, "7th")

# Call methods
student1.display()
student2.display()
