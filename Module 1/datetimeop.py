# ==========================================
# M1 Activity: Date and Time Operations
# ==========================================

# Import the datetime module
import datetime

# Get the current date and time
current = datetime.datetime.now()

# Display the current date and time
print("Current Date and Time:", current)

# Display only the date
print("Current Date:", current.date())

# Display only the time
print("Current Time:", current.time())

# Display individual components
print("Year:", current.year)
print("Month:", current.month)
print("Day:", current.day)
print("Hour:", current.hour)
print("Minute:", current.minute)
print("Second:", current.second)

# Display the date and time in a formatted way
formatted = current.strftime("%d-%m-%Y %I:%M:%S %p")
print("Formatted Date and Time:", formatted)
