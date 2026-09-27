# Python program to demonstrate
# Insert and Search operation in Binary Search Tree


# Class representing a node in BST
class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


# Function to insert a new value into BST
def insert_node(root, value):

    # If tree is empty, create a new node
    if root is None:
        return TreeNode(value)

    # If value already exists, do nothing
    if root.value == value:
        return root

    # If value is greater, insert into right subtree
    elif value > root.value:
        root.right = insert_node(root.right, value)

    # If value is smaller, insert into left subtree
    else:
        root.left = insert_node(root.left, value)

    return root


# Function to perform inorder traversal
def inorder_traversal(root):

    if root:
        # Visit left subtree
        inorder_traversal(root.left)

        # Print root value
        print(root.value)

        # Visit right subtree
        inorder_traversal(root.right)


# Creating the following BST
#
#          50
#        /    \
#       30     70
#      /  \   /  \
#     20  40 60  80

root = TreeNode(50)

# Insert values into the BST
root = insert_node(root, 30)
root = insert_node(root, 20)
root = insert_node(root, 40)
root = insert_node(root, 70)
root = insert_node(root, 60)
root = insert_node(root, 80)


# Print inorder traversal
inorder_traversal(root)
