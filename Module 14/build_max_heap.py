# Python program to build
# a Max Heap from an array


# Function to maintain Max Heap property
def heapify(array, heap_size, root_index):

    # Assume the root is the largest
    largest_index = root_index

    # Find left child
    left_index = 2 * root_index + 1

    # Find right child
    right_index = 2 * root_index + 2

    # Check if left child is larger than root
    if (
        left_index < heap_size
        and array[root_index] < array[left_index]
    ):
        largest_index = left_index

    # Check if right child is larger
    if (
        right_index < heap_size
        and array[largest_index] < array[right_index]
    ):
        largest_index = right_index

    # If the largest element is not the root,
    # swap them
    if largest_index != root_index:

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


# Unsorted array
array = [4, 10, 3, 5, 1]

# Number of elements
heap_size = len(array)


# Build Max Heap
for index in range(
    heap_size - 1,
    -1,
    -1
):
    heapify(
        array,
        heap_size,
        index
    )


# Display the Max Heap
print("Max Heap:", array)
