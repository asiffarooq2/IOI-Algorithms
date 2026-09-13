# Python program to implement a Stack using two Queues

from collections import deque


class Stack:
    def __init__(self):
        # Create two queues
        self.primary_queue = deque()
        self.secondary_queue = deque()

    # Push an element onto the stack
    def push(self, value):

        # Add the new element to the empty secondary queue
        self.secondary_queue.append(value)

        # Move all elements from the primary queue
        # to the secondary queue
        while self.primary_queue:
            self.secondary_queue.append(
                self.primary_queue.popleft()
            )

        # Swap the queues
        self.primary_queue, self.secondary_queue = (
            self.secondary_queue,
            self.primary_queue
        )

    # Remove the top element from the stack
    def pop(self):
        if self.primary_queue:
            self.primary_queue.popleft()
        else:
            print("Stack is empty")

    # Return the top element
    def top(self):
        if self.primary_queue:
            return self.primary_queue[0]

        return None

    # Return the number of elements
    def get_size(self):
        return len(self.primary_queue)


# Main program
if __name__ == '__main__':

    my_stack = Stack()

    # Push elements onto the stack
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)

    print("Current size:", my_stack.get_size())

    print("Top element:", my_stack.top())

    my_stack.pop()
    print("Top element after pop:", my_stack.top())

    my_stack.pop()
    print("Top element after pop:", my_stack.top())

    print("Current size:", my_stack.get_size())
