# Python program to implement Deque using a Doubly Linked List


# Node of a Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


# Deque implementation
class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.element_count = 0

    # Check whether the deque is empty
    def is_empty(self):
        return self.front is None

    # Return the number of elements
    def get_size(self):
        return self.element_count

    # Insert an element at the front
    def insert_front(self, data):
        new_node = Node(data)

        # If deque is empty
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            new_node.next = self.front
            self.front.previous = new_node
            self.front = new_node

        self.element_count += 1

    # Insert an element at the rear
    def insert_rear(self, data):
        new_node = Node(data)

        # If deque is empty
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            new_node.previous = self.rear
            self.rear.next = new_node
            self.rear = new_node

        self.element_count += 1

    # Delete an element from the front
    def delete_front(self):
        if self.is_empty():
            print("Underflow")
            return

        removed_node = self.front
        self.front = self.front.next

        # If deque becomes empty
        if self.front is None:
            self.rear = None
        else:
            self.front.previous = None

        self.element_count -= 1

    # Delete an element from the rear
    def delete_rear(self):
        if self.is_empty():
            print("Underflow")
            return

        removed_node = self.rear
        self.rear = self.rear.previous

        # If deque becomes empty
        if self.rear is None:
            self.front = None
        else:
            self.rear.next = None

        self.element_count -= 1

    # Get the front element
    def get_front(self):
        if self.is_empty():
            return -1

        return self.front.data

    # Get the rear element
    def get_rear(self):
        if self.is_empty():
            return -1

        return self.rear.data

    # Delete all elements from the deque
    def clear(self):
        self.front = None
        self.rear = None
        self.element_count = 0


# Main program
if __name__ == "__main__":

    my_deque = Deque()

    print("Insert element '5' at rear end")
    my_deque.insert_rear(5)

    print("Insert element '10' at rear end")
    my_deque.insert_rear(10)

    print("Rear end element:", my_deque.get_rear())

    my_deque.delete_rear()

    print(
        "After deleting rear element, new rear is:",
        my_deque.get_rear()
    )

    print("Inserting element '15' at front end")
    my_deque.insert_front(15)

    print("Front end element:", my_deque.get_front())

    print("Number of elements in Deque:", my_deque.get_size())

    my_deque.delete_front()

    print(
        "After deleting front element, new front is:",
        my_deque.get_front()
    )
