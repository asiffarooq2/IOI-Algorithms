# ================================
# OPERATIONS ON SETS
# SPORTS CLUB
# ================================

# Create a set
sports = {"Cricket", "Football", "Tennis", "Badminton"}

print("Sports Set:", sports)

# Find the number of elements
print("\nTotal Sports:", len(sports))

# Add a new element
sports.add("Basketball")
print("\nAfter Adding Basketball:", sports)

# Add multiple elements
sports.update(["Hockey", "Volleyball"])
print("After Adding More Sports:", sports)

# Remove an element
sports.remove("Tennis")
print("After Removing Tennis:", sports)

# Discard an element
sports.discard("Kabaddi")   # No error if the element is not present
print("After Discarding Kabaddi:", sports)

# Check if an element exists
print("\nIs Cricket Available?", "Cricket" in sports)
print("Is Chess Available?", "Chess" in sports)

# Create another set
indoor_games = {"Chess", "Carrom", "Badminton", "Table Tennis"}

print("\nIndoor Games:", indoor_games)

# Union
print("\nUnion:", sports.union(indoor_games))

# Intersection
print("Intersection:", sports.intersection(indoor_games))

# Difference
print("Difference (Sports - Indoor):", sports.difference(indoor_games))

# Symmetric Difference
print("Symmetric Difference:", sports.symmetric_difference(indoor_games))

# Loop through the set
print("\nAvailable Sports:")
for game in sports:
    print(game)

# Clear the set
sports.clear()
print("\nAfter Clearing the Set:", sports)
