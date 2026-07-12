# ================================
# OPERATIONS ON DICTIONARY
# STUDENT PROFILE
# ================================

# Create a dictionary
student = {
    "name": "Ayaan",
    "age": 14,
    "grade": "8th",
    "city": "Delhi"
}

print("Student Dictionary:", student)

# Access values
print("\nStudent Name:", student["name"])
print("Student Grade:", student["grade"])

# Using get()
print("Student Age:", student.get("age"))
print("Phone Number:", student.get("phone", "Not Available"))

# Update a value
student["grade"] = "9th"
print("\nAfter Updating Grade:", student)

# Add a new key-value pair
student["school"] = "Green Valley School"
print("After Adding School:", student)

# Remove a key-value pair
student.pop("city")
print("After Removing City:", student)

# Display dictionary keys
print("\nKeys:", student.keys())

# Display dictionary values
print("Values:", student.values())

# Display all key-value pairs
print("Items:", student.items())

# Check if a key exists
print("\nIs 'age' present?", "age" in student)

# Find total number of key-value pairs
print("Total Entries:", len(student))

# Clear the dictionary
student.clear()
print("\nAfter Clearing Dictionary:", student)
