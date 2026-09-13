# Python program to create a Binary Tree
# and perform In-order, Pre-order, and Post-order traversals

# Install the binarytree module if needed:
# pip install binarytree

from binarytree import Node


# Create the root node
root_node = Node(1)

# Create left and right children
root_node.left = Node(2)
root_node.right = Node(3)

# Add nodes to the left subtree
root_node.left.left = Node(4)
root_node.left.right = Node(5)

# Add nodes to the right subtree
root_node.right.left = Node(6)
root_node.right.right = Node(7)


# Display the binary tree
print("Binary Tree Structure:")
print(root_node)


# In-order Traversal
# Left → Root → Right
def in_order_traversal(current_node):
    if current_node:
        in_order_traversal(current_node.left)
        print(current_node.value, end=" ")
        in_order_traversal(current_node.right)


# Pre-order Traversal
# Root → Left → Right
def pre_order_traversal(current_node):
    if current_node:
        print(current_node.value, end=" ")
        pre_order_traversal(current_node.left)
        pre_order_traversal(current_node.right)


# Post-order Traversal
# Left → Right → Root
def post_order_traversal(current_node):
    if current_node:
        post_order_traversal(current_node.left)
        post_order_traversal(current_node.right)
        print(current_node.value, end=" ")


# Display In-order Traversal
print("\nIn-order Traversal:")
in_order_traversal(root_node)

# Display Pre-order Traversal
print("\nPre-order Traversal:")
pre_order_traversal(root_node)

# Display Post-order Traversal
print("\nPost-order Traversal:")
post_order_traversal(root_node)