# Program to implement two stacks in a single array/list

import math


class TwoStacks:
    def __init__(self, array_size):
        self.array_size = array_size
        self.stack_array = [None] * array_size

        # Stack 1 grows from the middle towards the beginning
        self.stack1_top = math.floor(array_size / 2) + 1

        # Stack 2 grows from the middle towards the end
        self.stack2_top = math.floor(array_size / 2)

    # Push an element into Stack 1
    def push_stack1(self, value):
        if self.stack1_top > 0:
            self.stack1_top = self.stack1_top - 1
            self.stack_array[self.stack1_top] = value
        else:
            print("Stack 1 Overflow by element:", value)

    # Push an element into Stack 2
    def push_stack2(self, value):
        if self.stack2_top < self.array_size - 1:
            self.stack2_top = self.stack2_top + 1
            self.stack_array[self.stack2_top] = value
        else:
            print("Stack 2 Overflow by element:", value)

    # Pop an element from Stack 1
    def pop_stack1(self):
        if self.stack1_top <= self.array_size / 2:
            removed_value = self.stack_array[self.stack1_top]
            self.stack1_top = self.stack1_top + 1
            return removed_value
        else:
            print("Stack 1 Underflow")
            return None

    # Pop an element from Stack 2
    def pop_stack2(self):
        if self.stack2_top >= math.floor(self.array_size / 2) + 1:
            removed_value = self.stack_array[self.stack2_top]
            self.stack2_top = self.stack2_top - 1
            return removed_value
        else:
            print("Stack 2 Underflow")
            return None


# Main program
two_stack = TwoStacks(5)

# Push elements into Stack 1
two_stack.push_stack1(5)
two_stack.push_stack1(13)

# Push elements into Stack 2
two_stack.push_stack2(10)
two_stack.push_stack2(10)
two_stack.push_stack2(6)

# Pop elements
print("Popped element from Stack 1 is:", two_stack.pop_stack1())

two_stack.push_stack2(12)

print("Popped element from Stack 2 is:", two_stack.pop_stack2())
