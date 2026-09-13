# Program to implement Stack using a Linked List


# Create a Node for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create a Stack using Linked List
class Stack:
    def __init__(self):
        self.top = None

    # Push an element onto the stack
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(data, "pushed to stack")

    # Pop an element from the stack
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return

        removed_data = self.top.data
        self.top = self.top.next
        print(removed_data, "popped from stack")

    # Display the top element
    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element is:", self.top.data)

    # Display all elements of the stack
    def display(self):
        if self.top is None:
            print("Stack is empty")
            return

        current_node = self.top

        print("Stack elements:")

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


# Create a stack
my_stack = Stack()

# Push elements
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

# Display the stack
my_stack.display()

# View the top element
my_stack.peek()

# Pop an element
my_stack.pop()

# Display the stack after popping
my_stack.display()
