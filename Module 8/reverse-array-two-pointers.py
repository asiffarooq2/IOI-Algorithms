# ==========================================
# REVERSE ARRAY USING TWO POINTERS
# ==========================================

# Array with different values
numbers = [10, 20, 30, 40, 50, 60, 70]

print("Original Array:")
print(numbers)


# Initialize start and end pointers
start = 0
end = len(numbers) - 1


# Reverse the same array
while start < end:

    # Swap elements at start and end
    numbers[start], numbers[end] = (
        numbers[end],
        numbers[start]
    )

    # Move start pointer forward
    start += 1

    # Move end pointer backward
    end -= 1


# Display reversed array
print("\nReversed Array:")
print(numbers)
