# ==========================================
# SORT ARRAY BY FREQUENCY AND INDEX
# ==========================================


# Class to store information about each value
class Data:

    def __init__(self, value, index, count=0):

        self.value = value
        self.index = index
        self.count = count


# Function to sort elements by
# frequency and first occurrence
def sortByFrequencyAndIndex(numbers):

    # Check if array is empty
    # or contains only one element
    if numbers is None or len(numbers) < 2:
        return

    # Dictionary to store values
    data_map = {}

    # Store frequency and index of
    # first occurrence of each element
    for i in range(len(numbers)):

        data_map.setdefault(
            numbers[i],
            Data(numbers[i], i)
        ).count += 1

    # Get Data objects from dictionary
    values = list(data_map.values())

    # Sort using:
    # 1. Higher frequency first
    # 2. Earlier occurrence first
    values.sort(
        key=lambda x: (
            -x.count,
            x.index
        )
    )

    # Rewrite the original array
    index = 0

    for data in values:

        for j in range(data.count):

            numbers[index] = data.value
            index += 1


# Driver Code
if __name__ == '__main__':

    numbers = [
        5, 2, 5, 7, 2,
        5, 9, 7, 7, 7,
        2, 4
    ]

    print(
        "Original Array:",
        numbers
    )

    sortByFrequencyAndIndex(numbers)

    print(
        "Sorted Array:",
        numbers
    )
