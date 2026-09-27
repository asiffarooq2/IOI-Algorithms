# Python program to implement
# Max Heap insertion and deletion


# Function to maintain Max Heap property
def heapify(heap, heap_size, root_index):

    # Assume the root is the largest
    largest_index = root_index

    # Find left and right child indexes
    left_index = 2 * root_index + 1
    right_index = 2 * root_index + 2

    # Check if left child is larger
    if (
        left_index < heap_size
        and heap[largest_index] < heap[left_index]
    ):
        largest_index = left_index

    # Check if right child is larger
    if (
        right_index < heap_size
        and heap[largest_index] < heap[right_index]
    ):
        largest_index = right_index

    # If a child is larger than the root,
    # swap them and continue heapifying
    if largest_index != root_index:

        heap[root_index], heap[largest_index] = (
            heap[largest_index],
            heap[root_index]
        )

        heapify(
            heap,
            heap_size,
            largest_index
        )


# Function to insert a new value
def insert_value(heap, value):

    # Add the new value
    heap.append(value)

    # Rebuild the Max Heap
    for index in range(
        len(heap) // 2 - 1,
        -1,
        -1
    ):

        heapify(
            heap,
            len(heap),
            index
        )


# Function to delete a value
def delete_value(heap, value):

    heap_size = len(heap)

    # Check if heap is empty
    if heap_size == 0:
        return

    # Search for the value
    for index in range(heap_size):

        if value == heap[index]:
            break

    else:
        # Value not found
        return

    # Replace the value with the last element
    heap[index], heap[heap_size - 1] = (
        heap[heap_size - 1],
        heap[index]
    )

    # Remove the last element
    heap.pop()

    # Rebuild the Max Heap
    for index in range(
        len(heap) // 2 - 1,
        -1,
        -1
    ):

        heapify(
            heap,
            len(heap),
            index
        )


# Create an empty heap
max_heap = []


# Insert values
insert_value(max_heap, 3)
insert_value(max_heap, 4)
insert_value(max_heap, 9)
insert_value(max_heap, 5)
insert_value(max_heap, 2)


# Display Max Heap
print("Max-Heap array:", max_heap)


# Delete value 4
delete_value(max_heap, 4)


# Display heap after deletion
print(
    "After deleting an element:",
    max_heap
)
