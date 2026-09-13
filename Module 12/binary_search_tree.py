# Python program to implement a Binary Search Tree (BST)


# Create a node for the Binary Search Tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    # Insert a new value into the Binary Search Tree
    def insert(self, value):

        # If the new value is smaller, go to the left subtree
        if value < self.value:

            if self.left_child is None:
                self.left_child = Node(value)
                print(
                    f"Inserted {value} to the left of {self.value}"
                )
            else:
                self.left_child.insert(value)

        # If the new value is larger, go to the right subtree
        elif value > self.value:

            if self.right_child is None:
                self.right_child = Node(value)
                print(
                    f"Inserted {value} to the right of {self.value}"
                )
            else:
                self.right_child.insert(value)

        # Duplicate value
        else:
            print(
                f"Value {value} already exists in the tree."
            )

    # Perform In-order Traversal
    def print_tree(self):

        # Visit the left subtree
        if self.left_child:
            self.left_child.print_tree()

        # Visit the current node
        print(self.value, end=" ")

        # Visit the right subtree
        if self.right_child:
            self.right_child.print_tree()


# Main program

# Create the root node
root_node = Node(12)

# Insert values into the Binary Search Tree
root_node.insert(6)
root_node.insert(14)
root_node.insert(3)

# Display the tree using In-order Traversal
print("In-order Traversal:")
root_node.print_tree()
