from sys import maxsize


def create_stack():
    stack = []
    return stack


def is_stack_empty(stack):
    return len(stack) == 0


def push_item(stack, value):
    stack.append(value)
    print(value + " pushed to stack")


def pop_item(stack):
    if is_stack_empty(stack):
        return str(-maxsize - 1)
    return stack.pop()


def peek_item(stack):
    if is_stack_empty(stack):
        return str(-maxsize - 1)
    return stack[len(stack) - 1]


# Create a stack
my_stack = create_stack()

# Push items into the stack
push_item(my_stack, str(10))
push_item(my_stack, str(20))
push_item(my_stack, str(30))

# Pop an item from the stack
print(pop_item(my_stack) + " popped from stack")