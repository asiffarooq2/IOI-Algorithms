import sys


# Class representing an element
# in the priority queue
class PriorityItem:

    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


# Class representing the Priority Queue
class PriorityQueue:

    def __init__(self):
        # Store priority queue elements
        self.queue = [None] * 100000

        # Index of the last element
        self.size = -1

    # Function to insert an element
    # into the priority queue

    def enqueue(self, value, priority):

        # Increase the size
        self.size += 1

        # Create a new priority item
        self.queue[self.size] = PriorityItem(
            value,
            priority
        )

    # Function to find the position
    # of the highest-priority element

    def peek(self):

        highest_priority = -sys.maxsize
        highest_index = -1

        # Search through all elements
        for index in range(self.size + 1):

            # If priorities are equal,
            # choose the element with
            # the larger value
            if (
                highest_priority == self.queue[index].priority
                and highest_index > -1
                and self.queue[highest_index].value
                < self.queue[index].value
            ):

                highest_priority = self.queue[index].priority
                highest_index = index

            # If current priority is higher
            elif (
                highest_priority
                < self.queue[index].priority
            ):

                highest_priority = (
                    self.queue[index].priority
                )

                highest_index = index

        return highest_index

    # Function to remove the element
    # with the highest priority

    def dequeue(self):

        # Find highest-priority element
        highest_index = self.peek()

        # Shift elements to fill the empty position
        for index in range(
            highest_index,
            self.size
        ):

            self.queue[index] = (
                self.queue[index + 1]
            )

        # Reduce queue size
        self.size -= 1


# Main program
if __name__ == "__main__":

    # Create a priority queue
    priority_queue = PriorityQueue()

    # Insert elements
    priority_queue.enqueue(10, 2)
    priority_queue.enqueue(14, 4)
    priority_queue.enqueue(16, 4)
    priority_queue.enqueue(12, 3)

    # Get highest-priority element
    highest_index = priority_queue.peek()

    print(
        priority_queue.queue[highest_index].value
    )

    # Remove highest-priority element
    priority_queue.dequeue()

    # Get next highest-priority element
    highest_index = priority_queue.peek()

    print(
        priority_queue.queue[highest_index].value
    )

    # Remove highest-priority element
    priority_queue.dequeue()

    # Get next highest-priority element
    highest_index = priority_queue.peek()

    print(
        priority_queue.queue[highest_index].value
    )
