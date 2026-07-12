# ================================
# EMPLOYEE CLASS
# ================================

# Create a class
class Employee:

    # Constructor
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    # Method to display employee details
    def display(self):
        print("\nEmployee Details")
        print("-------------------------")
        print("Employee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Department  :", self.department)
        print("Salary      : ₹", self.salary)

    # Method to increase salary
    def increment(self, amount):
        self.salary += amount
        print("\nSalary Increased by ₹", amount)
        print("New Salary: ₹", self.salary)


# Create objects
employee1 = Employee(101, "Rahul", "HR", 35000)
employee2 = Employee(102, "Priya", "IT", 50000)

# Display employee details
employee1.display()
employee2.display()

# Increase salary
employee1.increment(5000)

# Display updated details
employee1.display()
