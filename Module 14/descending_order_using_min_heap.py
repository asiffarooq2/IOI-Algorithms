import heapq


# Function to sort an array in descending order
def sort_descending(array):

    # Create an empty Min Heap
    min_heap = []

    # Insert all elements into the Min Heap
    for value in array:
        heapq.heappush(min_heap, value)

    # Store the sorted elements
    sorted_array = []

    # Remove elements from Min Heap
    while min_heap:

        # Remove the smallest element
        smallest_value = heapq.heappop(min_heap)

        # Insert it at the beginning
        # to create descending order
        sorted_array.insert(0, smallest_value)

    return sorted_array


# Main program
if __name__ == "__main__":

    # Given array
    array = [4, 6, 3, 2, 9]

    # Sort the array in descending order
    result = sort_descending(array)

    # Display the result
    for value in result:
        print(value, end=" ")

    print()
