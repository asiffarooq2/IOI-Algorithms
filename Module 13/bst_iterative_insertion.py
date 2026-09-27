# Python program to implement
# BST insertion operation iteratively


# Class representing a node in BST
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Class representing the Binary Search Tree
class BinarySearchTree:

    def __init__(self):
        self.root = None

    # Function to insert a value into BST
    def insert(self, value):

        # Create a new node
        new_node = TreeNode(value)

        # If tree is empty, make new node the root
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        parent = None

        # Find the correct position for the new node
        while current is not None:

            parent = current

            # Move to the left if value is smaller
            if value < current.value:
                current = current.left

            # Move to the right if value is larger
            elif value > current.value:
                current = current.right

            # Duplicate value
            else:
                return

        # Attach the new node to its parent
        if value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

    # Function to perform inorder traversal
    # without recursion
    def inorder_traversal(self):

        current = self.root
        stack = []

        while current is not None or len(stack) > 0:

            # Go to the leftmost node
            if current is not None:
                stack.append(current)
                current = current.left

            else:
                # Remove the top node from stack
                current = stack.pop()

                # Print the node
                print(current.value, end=" ")

                # Move to the right subtree
                current = current.right


# Main program
if __name__ == "__main__":

    tree = BinarySearchTree()

    # Insert values into BST
    tree.insert(30)
    tree.insert(50)
    tree.insert(15)
    tree.insert(20)
    tree.insert(10)
    tree.insert(40)
    tree.insert(60)

    # Display inorder traversal
    tree.inorder_traversal()
