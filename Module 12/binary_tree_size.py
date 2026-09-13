class BinaryTreeNode:
    """Represents a node in a binary tree."""

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


def calculate_tree_size_recursive(root):
    """Calculate the total number of nodes using recursion."""

    if root is None:
        return 0

    left_size = calculate_tree_size_recursive(root.left_child)
    right_size = calculate_tree_size_recursive(root.right_child)

    return left_size + right_size + 1


def calculate_tree_size_iterative(root):
    """Calculate the total number of nodes using a stack."""

    if root is None:
        return 0

    node_count = 0
    node_stack = [root]

    while node_stack:
        current_node = node_stack.pop()
        node_count += 1

        if current_node.left_child is not None:
            node_stack.append(current_node.left_child)

        if current_node.right_child is not None:
            node_stack.append(current_node.right_child)

    return node_count


# Create the binary tree
root = BinaryTreeNode(1)

root.left_child = BinaryTreeNode(2)
root.right_child = BinaryTreeNode(3)

root.left_child.left_child = BinaryTreeNode(4)
root.left_child.right_child = BinaryTreeNode(5)

root.right_child.left_child = BinaryTreeNode(6)
root.right_child.right_child = BinaryTreeNode(7)

root.right_child.left_child.left_child = BinaryTreeNode(8)
root.right_child.left_child.right_child = BinaryTreeNode(9)


# Calculate tree size using recursion
recursive_size = calculate_tree_size_recursive(root)
print(f"Size of the binary tree (recursive): {recursive_size}")


# Calculate tree size using iteration
iterative_size = calculate_tree_size_iterative(root)
print(f"Size of the binary tree (iterative): {iterative_size}")
