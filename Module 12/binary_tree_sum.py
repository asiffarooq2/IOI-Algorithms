class BinaryTreeNode:
    """Represents a node in a binary tree."""

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


def calculate_tree_sum(root):
    """Calculate the sum of all nodes in the binary tree recursively."""

    if root is None:
        return 0

    left_sum = calculate_tree_sum(root.left_child)
    right_sum = calculate_tree_sum(root.right_child)

    return left_sum + right_sum + root.value


if __name__ == "__main__":
    # Create the binary tree
    root = BinaryTreeNode(10)

    root.left_child = BinaryTreeNode(20)
    root.right_child = BinaryTreeNode(30)

    root.left_child.left_child = BinaryTreeNode(40)
    root.left_child.right_child = BinaryTreeNode(50)

    root.right_child.left_child = BinaryTreeNode(60)
    root.right_child.right_child = BinaryTreeNode(70)

    root.right_child.left_child.right_child = BinaryTreeNode(80)

    # Calculate the sum of all nodes
    total_sum = calculate_tree_sum(root)

    print(f"Sum of all nodes: {total_sum}")
