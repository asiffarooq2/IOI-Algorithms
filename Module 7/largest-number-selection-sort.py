# ==========================================
# LARGEST POSSIBLE NUMBER
# USING SELECTION SORT
# ==========================================


# Function to compare two numbers
def compare(num1, num2):

    return (
        str(num1) + str(num2)
        >
        str(num2) + str(num1)
    )


# Selection Sort
def largestNumber(numbers):

    for i in range(len(numbers), 0, -1):

        temp = 0

        for j in range(i):

            if not compare(
                numbers[j],
                numbers[temp]
            ):
                temp = j

        # Swap elements
        numbers[temp], numbers[i - 1] = (
            numbers[i - 1],
            numbers[temp]
        )

    # Join all numbers together
    return str(
        int(
            "".join(
                map(str, numbers)
            )
        )
    )


# Driver Code
numbers = [12, 121, 45, 9, 34, 3]

print(
    "Given Array:",
    numbers
)

print(
    "Largest Possible Number:",
    largestNumber(numbers)
)
