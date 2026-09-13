class BinaryTreeNode:
    """Represents a node in a binary tree."""

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


def calculate_tree_height(root):
    """Calculate the height of the binary tree recursively."""

    if root is None:
        return 0

    left_height = calculate_tree_height(root.left_child)
    right_height = calculate_tree_height(root.right_child)

    return max(left_height, right_height) + 1


if __name__ == "__main__":
    # Create the binary tree
    root = BinaryTreeNode(1)

    root.left_child = BinaryTreeNode(2)
    root.right_child = BinaryTreeNode(3)

    root.left_child.left_child = BinaryTreeNode(4)
    root.left_child.right_child = BinaryTreeNode(5)

    # Calculate the height of the tree
    tree_height = calculate_tree_height(root)

    print(f"Height of the tree: {tree_height}")
