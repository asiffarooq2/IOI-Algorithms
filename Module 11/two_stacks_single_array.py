# Python program to implement two stacks in a single list


class TwoStacks:
    def __init__(self, list_size):
        self.list_size = list_size
        self.stack_list = [None] * list_size

        # Stack 1 starts from the beginning
        self.stack1_top = -1

        # Stack 2 starts from the end
        self.stack2_top = self.list_size

    # Push an element into Stack 1
    def push_stack1(self, value):
        if self.stack1_top < self.stack2_top - 1:
            self.stack1_top = self.stack1_top + 1
            self.stack_list[self.stack1_top] = value
        else:
            print("Stack Overflow")
            return

    # Push an element into Stack 2
    def push_stack2(self, value):
        if self.stack1_top < self.stack2_top - 1:
            self.stack2_top = self.stack2_top - 1
            self.stack_list[self.stack2_top] = value
        else:
            print("Stack Overflow")
            return

    # Pop an element from Stack 1
    def pop_stack1(self):
        if self.stack1_top >= 0:
            removed_value = self.stack_list[self.stack1_top]
            self.stack1_top = self.stack1_top - 1
            return removed_value
        else:
            print("Stack Underflow")
            return None

    # Pop an element from Stack 2
    def pop_stack2(self):
        if self.stack2_top < self.list_size:
            removed_value = self.stack_list[self.stack2_top]
            self.stack2_top = self.stack2_top + 1
            return removed_value
        else:
            print("Stack Underflow")
            return None


# Main program

two_stack = TwoStacks(5)

# Add elements to Stack 1
two_stack.push_stack1(5)
two_stack.push_stack1(16)
two_stack.push_stack1(26)

# Add elements to Stack 2
two_stack.push_stack2(10)
two_stack.push_stack2(13)

# Remove an element from Stack 1
print("Popped element from Stack 1 is:", two_stack.pop_stack1())

# Add another element to Stack 2
two_stack.push_stack2(12)

# Remove an element from Stack 2
print("Popped element from Stack 2 is:", two_stack.pop_stack2())
