# ==========================================
# M1 Activity: Fibonacci Series
# ==========================================

# Take input from the user
n = int(input("Enter the number of terms: "))

# First two terms
a = 0
b = 1

print("Fibonacci Series:")

# Generate the series
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
