# Python program to implement
# Heap Sort


# Function to maintain Max Heap property
def heapify(array, heap_size, root_index):

    # Assume the root is the largest
    largest_index = root_index

    # Find left child
    left_index = 2 * root_index + 1

    # Find right child
    right_index = 2 * root_index + 2

    # Check if left child is larger
    if (
        left_index < heap_size
        and array[left_index] > array[largest_index]
    ):
        largest_index = left_index

    # Check if right child is larger
    if (
        right_index < heap_size
        and array[right_index] > array[largest_index]
    ):
        largest_index = right_index

    # If a child is larger than the root
    if largest_index != root_index:

        # Swap root with the largest child
        array[root_index], array[largest_index] = (
            array[largest_index],
            array[root_index]
        )

        # Heapify the affected subtree
        heapify(
            array,
            heap_size,
            largest_index
        )


# Function to perform Heap Sort
def heap_sort(array):

    array_size = len(array)

    # Step 1: Build a Max Heap
    for index in range(
        array_size // 2 - 1,
        -1,
        -1
    ):

        heapify(
            array,
            array_size,
            index
        )

    # Step 2: Move the largest element
    # to the end one by one
    for last_index in range(
        array_size - 1,
        0,
        -1
    ):

        # Move maximum element to the end
        array[0], array[last_index] = (
            array[last_index],
            array[0]
        )

        # Restore Max Heap property
        heapify(
            array,
            last_index,
            0
        )


# Main program
if __name__ == "__main__":

    # Unsorted array
    array = [12, 11, 13, 5, 6, 7]

    # Perform Heap Sort
    heap_sort(array)

    # Display sorted array
    print("Sorted array is:")

    for value in array:
        print(value, end=" ")
