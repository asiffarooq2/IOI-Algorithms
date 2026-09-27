# Python program to search
# for a value in a Binary Search Tree


# Class representing a node in BST
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Function to search for a value in BST
def search_node(root, target):

    # Base case:
    # Tree is empty OR target is found
    if root is None or root.value == target:
        return root

    # If target is greater than current node,
    # search in the right subtree
    if target > root.value:
        return search_node(root.right, target)

    # If target is smaller than current node,
    # search in the left subtree
    return search_node(root.left, target)


# Create the following BST
#
#          50
#        /    \
#       30     70
#      /  \   /  \
#     20  40 60  80

root = TreeNode(50)

root.left = TreeNode(30)
root.right = TreeNode(70)

root.left.left = TreeNode(20)
root.left.right = TreeNode(40)

root.right.left = TreeNode(60)
root.right.right = TreeNode(80)


# Get the value to search from the user
target = int(input("Enter value to search: "))

# Search for the value
result = search_node(root, target)


# Display the result
if result:
    print("Value found:", result.value)
else:
    print("Value not found")
