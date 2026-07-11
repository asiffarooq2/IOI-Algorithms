# ==========================================
# M1 Activity: Sum of Natural Numbers
# ==========================================

# Take input from the user
n = int(input("Enter a positive number: "))

# Initialize sum
total = 0

# Calculate the sum
for i in range(1, n + 1):
    total = total + i

# Display the result
print("The sum of the first", n, "natural numbers is:", total)
