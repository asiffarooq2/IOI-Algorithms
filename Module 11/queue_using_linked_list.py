# Python program to implement Queue using a Linked List


# Create a Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None


# Create a Queue
class Queue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None

    # Check whether the queue is empty
    def is_empty(self):
        return self.front_node is None

    # Add an element to the queue
    def enqueue(self, value):
        new_node = Node(value)

        # If the queue is empty
        if self.rear_node is None:
            self.front_node = self.rear_node = new_node
            return

        # Add the new node at the rear
        self.rear_node.next_node = new_node
        self.rear_node = new_node

    # Remove an element from the queue
    def dequeue(self):
        # If the queue is empty
        if self.is_empty():
            return

        # Remove the front node
        removed_node = self.front_node
        self.front_node = removed_node.next_node

        # If the queue becomes empty
        if self.front_node is None:
            self.rear_node = None


# Main program
if __name__ == '__main__':

    my_queue = Queue()

    # Add elements
    my_queue.enqueue(10)
    my_queue.enqueue(20)

    # Remove elements
    my_queue.dequeue()
    my_queue.dequeue()

    # Add more elements
    my_queue.enqueue(30)
    my_queue.enqueue(40)
    my_queue.enqueue(50)

    # Remove one element
    my_queue.dequeue()

    # Display front and rear elements
    print(
        "Queue Front:",
        my_queue.front_node.value if my_queue.front_node is not None else -1
    )

    print(
        "Queue Rear:",
        my_queue.rear_node.value if my_queue.rear_node is not None else -1
    )
