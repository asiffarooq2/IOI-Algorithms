# Python program to demonstrate
# deletion operation in Binary Search Tree


# Class representing a node in BST
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Function to perform inorder traversal
def inorder_traversal(root):

    if root is not None:
        # Visit left subtree
        inorder_traversal(root.left)

        # Visit root
        print(root.value, end=" ")

        # Visit right subtree
        inorder_traversal(root.right)


# Function to insert a value into BST
def insert_node(root, value):

    # If tree is empty, create a new node
    if root is None:
        return TreeNode(value)

    # Insert smaller values into left subtree
    if value < root.value:
        root.left = insert_node(root.left, value)

    # Insert larger values into right subtree
    else:
        root.right = insert_node(root.right, value)

    return root


# Function to find the smallest node
# in a subtree
def find_minimum_node(root):

    current_node = root

    # Move to the leftmost node
    while current_node.left is not None:
        current_node = current_node.left

    return current_node


# Function to delete a node from BST
def delete_node(root, value):

    # Base case: tree is empty
    if root is None:
        return root

    # If value is smaller, search in left subtree
    if value < root.value:
        root.left = delete_node(root.left, value)

    # If value is larger, search in right subtree
    elif value > root.value:
        root.right = delete_node(root.right, value)

    # Value found
    else:

        # Case 1: Node has no left child
        # or only a right child
        if root.left is None:
            return root.right

        # Case 2: Node has only a left child
        elif root.right is None:
            return root.left

        # Case 3: Node has two children
        # Find the smallest node in right subtree
        successor = find_minimum_node(root.right)

        # Copy successor's value
        root.value = successor.value

        # Delete the successor
        root.right = delete_node(
            root.right,
            successor.value
        )

    return root


# Main program

# Creating the following BST
#
#          50
#        /    \
#       30     70
#      /  \   /  \
#     20  40 60  80

root = None

# Insert values into BST
root = insert_node(root, 50)
root = insert_node(root, 30)
root = insert_node(root, 20)
root = insert_node(root, 40)
root = insert_node(root, 70)
root = insert_node(root, 60)
root = insert_node(root, 80)


# Display original tree
print("Inorder traversal of the given tree:")
inorder_traversal(root)


# Delete node 20
print("\n\nDelete 20")
root = delete_node(root, 20)

print("Inorder traversal after deletion:")
inorder_traversal(root)


# Delete node 30
print("\n\nDelete 30")
root = delete_node(root, 30)

print("Inorder traversal after deletion:")
inorder_traversal(root)


# Delete node 50
print("\n\nDelete 50")
root = delete_node(root, 50)

print("Inorder traversal after deletion:")
inorder_traversal(root)
