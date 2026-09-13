class BinaryTreeNode:
    """Represents a node in a binary tree."""

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


def calculate_subtree_sum(root, total_tilt):
    """
    Calculate the sum of a subtree and update the total tree tilt.
    """

    if root is None:
        return 0

    # Calculate the sum of the left and right subtrees
    left_subtree_sum = calculate_subtree_sum(
        root.left_child,
        total_tilt
    )

    right_subtree_sum = calculate_subtree_sum(
        root.right_child,
        total_tilt
    )

    # Tilt of the current node
    current_tilt = abs(left_subtree_sum - right_subtree_sum)

    # Add current node's tilt to the total tilt
    total_tilt[0] += current_tilt

    # Return the sum of the current subtree
    return (
        left_subtree_sum
        + right_subtree_sum
        + root.value
    )


def calculate_tree_tilt(root):
    """Calculate the total tilt of the binary tree."""

    total_tilt = [0]

    calculate_subtree_sum(root, total_tilt)

    return total_tilt[0]


if __name__ == "__main__":
    # Create the binary tree
    root = BinaryTreeNode(4)

    root.left_child = BinaryTreeNode(2)
    root.right_child = BinaryTreeNode(9)

    root.left_child.left_child = BinaryTreeNode(3)
    root.left_child.right_child = BinaryTreeNode(8)

    root.right_child.right_child = BinaryTreeNode(7)

    # Calculate and display the total tree tilt
    tree_tilt = calculate_tree_tilt(root)

    print(f"The tilt of the whole tree is: {tree_tilt}")
