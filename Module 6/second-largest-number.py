# Function to find the second largest number
def findSecondLargest(numbers, size):

    largest = second_largest = -2147483648

    for i in range(size):

        # If current number is greater than largest
        if numbers[i] > largest:

            second_largest = largest
            largest = numbers[i]

        # If number is smaller than largest
        # but greater than second largest
        elif (
            numbers[i] > second_largest
            and numbers[i] != largest
        ):

            second_largest = numbers[i]

    print("Largest Number:", largest)
    print("Second Largest Number:", second_largest)


# Array with different values
numbers = [45, 12, 89, 34, 76, 105, 67, 98]

size = len(numbers)


print("Array:", numbers)

findSecondLargest(numbers, size)
