# ================================
# OPERATIONS ON TUPLES
# WEEKDAY SCHEDULE
# ================================

# Create a tuple
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

print("Weekdays:", weekdays)

# Access tuple elements
print("\nFirst Day:", weekdays[0])
print("Last Day:", weekdays[-1])

# Slicing
print("First Three Days:", weekdays[:3])
print("Last Two Days:", weekdays[3:])

# Find the length of the tuple
print("\nTotal Days:", len(weekdays))

# Count occurrences
days = ("Monday", "Tuesday", "Monday", "Friday", "Monday")
print("\nTuple with Repeated Days:", days)
print("Monday appears", days.count("Monday"), "times")

# Find the index of an element
print("Index of Thursday:", weekdays.index("Thursday"))

# Check if an item exists
print("\nIs 'Wednesday' in the tuple?", "Wednesday" in weekdays)
print("Is 'Sunday' in the tuple?", "Sunday" in weekdays)

# Concatenate tuples
weekend = ("Saturday", "Sunday")
full_week = weekdays + weekend
print("\nComplete Week:", full_week)

# Repeat a tuple
print("\nRepeated Tuple:", ("Break",) * 3)

# Loop through a tuple
print("\nDays of the Week:")
for day in full_week:
    print(day)

# Final Summary
print("\n================================")
print("TUPLE OPERATIONS COMPLETED")
print("================================")
