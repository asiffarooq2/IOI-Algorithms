# Python program to implement a Stack using two Queues

from collections import deque


class Stack:
    def __init__(self):
        # Create two queues
        self.primary_queue = deque()
        self.secondary_queue = deque()

    # Push an element onto the stack
    def push(self, value):
        self.primary_queue.append(value)

    # Remove the top element from the stack
    def pop(self):
        # Check if the stack is empty
        if not self.primary_queue:
            print("Stack is empty")
            return

        # Move all elements except the last one
        # from the primary queue to the secondary queue
        while len(self.primary_queue) != 1:
            self.secondary_queue.append(
                self.primary_queue.popleft()
            )

        # Remove the last element
        removed_value = self.primary_queue.popleft()

        # Swap the two queues
        self.primary_queue, self.secondary_queue = (
            self.secondary_queue,
            self.primary_queue
        )

        return removed_value

    # Return the top element without removing it
    def top(self):
        # Check if the stack is empty
        if not self.primary_queue:
            print("Stack is empty")
            return None

        # Move all elements except the last one
        # to the secondary queue
        while len(self.primary_queue) != 1:
            self.secondary_queue.append(
                self.primary_queue.popleft()
            )

        # The remaining element is the top
        top_value = self.primary_queue.popleft()

        # Put it back into the secondary queue
        self.secondary_queue.append(top_value)

        # Swap the two queues
        self.primary_queue, self.secondary_queue = (
            self.secondary_queue,
            self.primary_queue
        )

        return top_value

    # Return the number of elements in the stack
    def get_size(self):
        return len(self.primary_queue)


# Main program
if __name__ == '__main__':

    my_stack = Stack()

    # Push elements
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
