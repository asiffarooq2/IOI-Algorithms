# Python program to implement
# Max Binary Heap


class MaxBinaryHeap:

    def __init__(self):
        # List used to store heap elements
        self.heap = []

    # Function to get the number of elements

    def get_size(self):
        return len(self.heap)

    # Function to find parent index

    def get_parent_index(self, index):
        return (index - 1) // 2

    # Function to find left child index

    def get_left_child_index(self, index):
        return 2 * index + 1

    # Function to find right child index

    def get_right_child_index(self, index):
        return 2 * index + 2

    # Function to get element at a given index

    def get_element(self, index):
        return self.heap[index]

    # Function to get maximum value

    def get_maximum(self):

        if self.get_size() == 0:
            return None

        # Maximum value is always at the root
        return self.heap[0]

    # Function to remove and return maximum value

    def extract_maximum(self):

        # Check if heap is empty
        if self.get_size() == 0:
            return None

        # Store maximum value
        maximum_value = self.get_maximum()

        # Move last element to root
        self.heap[0] = self.heap[-1]

        # Remove last element
        del self.heap[-1]

        # Restore Max Heap property
        if self.get_size() > 0:
            self.max_heapify(0)

        return maximum_value

    # Function to maintain Max Heap property

    def max_heapify(self, index):

        # Find left and right children
        left_index = self.get_left_child_index(index)
        right_index = self.get_right_child_index(index)

        # Assume current node is largest
        largest_index = index

        # Check left child
        if (
            left_index < self.get_size()
            and self.get_element(left_index)
            > self.get_element(index)
        ):
            largest_index = left_index

        # Check right child
        if (
            right_index < self.get_size()
            and self.get_element(right_index)
            > self.get_element(largest_index)
        ):
            largest_index = right_index

        # If child is larger, swap
        if largest_index != index:

            self.swap_elements(
                largest_index,
                index
            )

            # Continue heapifying
            self.max_heapify(largest_index)

    # Function to swap two elements

    def swap_elements(self, first_index, second_index):

        self.heap[first_index], self.heap[second_index] = (
            self.heap[second_index],
            self.heap[first_index]
        )

    # Function to insert a new value

    def insert(self, value):

        # Insert value at the end
        current_index = self.get_size()
        self.heap.append(value)

        # Move the value upward
        # until Max Heap property is restored
        while current_index != 0:

            parent_index = self.get_parent_index(current_index)

            if (
                self.get_element(parent_index)
                < self.get_element(current_index)
            ):

                self.swap_elements(
                    parent_index,
                    current_index
                )

            else:
                # Stop if parent is already larger
                break

            current_index = parent_index


# Create a Max Binary Heap
max_heap = MaxBinaryHeap()


# Menu
print("Menu")
print("insert <value>")
print("max get")
print("max extract")
print("quit")


# Menu-driven program
while True:

    user_input = input(
        "What would you like to do? "
    ).split()

    operation = user_input[0].strip().lower()

    # Insert operation
    if operation == "insert":

        value = int(user_input[1])

        max_heap.insert(value)

    # Maximum operations
    elif operation == "max":

        sub_operation = user_input[1].strip().lower()

        # Get maximum value
        if sub_operation == "get":

            print(
                "Maximum value:",
                max_heap.get_maximum()
            )

        # Extract maximum value
        elif sub_operation == "extract":

            print(
                "Maximum value removed:",
                max_heap.extract_maximum()
            )

    # Exit program
    elif operation == "quit":

        break
