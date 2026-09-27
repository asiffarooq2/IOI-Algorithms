# Python program to implement
# Max Heap operations


class MaxHeap:

    # Constructor
    def __init__(self, maximum_size):

        # Maximum number of elements
        self.maximum_size = maximum_size

        # Create an empty array
        self.heap = [None] * maximum_size

        # Current number of elements
        self.size = 0

    # Function to maintain Max Heap property

    def heapify(self, index):

        # Find left and right child
        left_index = self.left_child(index)
        right_index = self.right_child(index)

        # Assume current node is the largest
        largest_index = index

        # Check left child
        if (
            left_index < self.size
            and self.heap[left_index] > self.heap[index]
        ):
            largest_index = left_index

        # Check right child
        if (
            right_index < self.size
            and self.heap[right_index]
            > self.heap[largest_index]
        ):
            largest_index = right_index

        # If a child is larger, swap
        if largest_index != index:

            self.heap[index], self.heap[largest_index] = (
                self.heap[largest_index],
                self.heap[index]
            )

            # Continue heapifying
            self.heapify(largest_index)

    # Function to find parent index

    def parent_index(self, index):
        return (index - 1) // 2

    # Function to find left child index

    def left_child(self, index):
        return 2 * index + 1

    # Function to find right child index

    def right_child(self, index):
        return 2 * index + 2

    # Function to remove maximum element

    def remove_max(self):

        # Check if heap is empty
        if self.size <= 0:
            return None

        # If there is only one element
        if self.size == 1:

            self.size -= 1
            return self.heap[0]

        # Store maximum element
        maximum_value = self.heap[0]

        # Move last element to root
        self.heap[0] = self.heap[self.size - 1]

        # Reduce heap size
        self.size -= 1

        # Restore Max Heap property
        self.heapify(0)

        return maximum_value

    # Function to increase the value
    # of an element

    def increase_key(self, index, new_value):

        self.heap[index] = new_value

        # Move the element upward
        # until Max Heap property is restored
        while (
            index != 0
            and self.heap[self.parent_index(index)]
            < self.heap[index]
        ):

            parent = self.parent_index(index)

            # Swap current element with parent
            self.heap[index], self.heap[parent] = (
                self.heap[parent],
                self.heap[index]
            )

            index = parent

    # Function to get maximum element

    def get_max(self):
        return self.heap[0]

    # Function to get current heap size

    def get_size(self):
        return self.size

    # Function to delete an element

    def delete_key(self, index):

        # Increase value to infinity
        self.increase_key(index, float("inf"))

        # Remove maximum element
        self.remove_max()

    # Function to insert a new value

    def insert_key(self, value):

        # Check if heap is full
        if self.size == self.maximum_size:

            print("\nOverflow: Could not insert value\n")
            return

        # Increase heap size
        self.size += 1

        # Position of new element
        index = self.size - 1

        # Insert value at the end
        self.heap[index] = value

        # Move the new element upward
        # until Max Heap property is restored
        while (
            index != 0
            and self.heap[self.parent_index(index)]
            < self.heap[index]
        ):

            parent = self.parent_index(index)

            # Swap with parent
            self.heap[index], self.heap[parent] = (
                self.heap[parent],
                self.heap[index]
            )

            index = parent


# Main program
if __name__ == "__main__":

    # Create a Max Heap with maximum size 15
    max_heap = MaxHeap(15)

    print(
        "Entered 6 values: "
        "3, 10, 12, 8, 2, 14\n"
    )

    # Insert values
    max_heap.insert_key(3)
    max_heap.insert_key(10)
    max_heap.insert_key(12)
    max_heap.insert_key(8)
    max_heap.insert_key(2)
    max_heap.insert_key(14)

    # Display current size
    print(
        "The current size of the heap is",
        max_heap.get_size()
    )

    # Display maximum element
    print(
        "The current maximum element is",
        max_heap.get_max()
    )

    # Delete element at index 2
    max_heap.delete_key(2)

    # Display size after deletion
    print(
        "The current size of the heap is",
        max_heap.get_size()
    )

    # Insert two more values
    max_heap.insert_key(15)
    max_heap.insert_key(5)

    print(
        "The current size of the heap is",
        max_heap.get_size()
    )

    print(
        "The current maximum element is",
        max_heap.get_max()
    )
