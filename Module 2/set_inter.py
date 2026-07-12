# ================================
# SET INTERSECTION
# STUDENT CLUBS
# ================================

# Create two sets
science_club = {"Aarav", "Priya", "Rahul", "Sneha", "Meera"}
sports_club = {"Rahul", "Sneha", "Kabir", "Riya", "Meera"}

print("Science Club:", science_club)
print("Sports Club:", sports_club)

# Intersection using intersection() method
common_students = science_club.intersection(sports_club)

print("\nStudents in Both Clubs:")
print(common_students)

# Intersection using & operator
common_students2 = science_club & sports_club

print("\nIntersection using & operator:")
print(common_students2)

print("\nTotal Common Students:", len(common_students))
