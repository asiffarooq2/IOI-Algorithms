import sys

sys.setrecursionlimit(1_000_000)

MIN_VALUE = -2_147_483_648
MAX_VALUE = 2_147_483_647


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


def find_largest_bst(root):
    """
    Returns:
        minimum_value, maximum_value, bst_size
    """

    if root is None:
        return MAX_VALUE, MIN_VALUE, 0

    # Leaf node is itself a BST of size 1.
    if root.left_child is None and root.right_child is None:
        return root.value, root.value, 1

    left_minimum, left_maximum, left_size = find_largest_bst(
        root.left_child
    )

    right_minimum, right_maximum, right_size = find_largest_bst(
        root.right_child
    )

    # Check whether the current tree is a valid BST.
    if left_maximum < root.value < right_minimum:
        minimum_value = min(left_minimum, right_minimum, root.value)
        maximum_value = max(left_maximum, right_maximum, root.value)
        bst_size = 1 + left_size + right_size

        return minimum_value, maximum_value, bst_size

    # Current tree is not a BST.
    # Return the size of the larger BST from either subtree.
    return MIN_VALUE, MAX_VALUE, max(left_size, right_size)


def calculate_largest_bst_size(root):
    """
    Returns the number of nodes in the largest BST
    present inside the binary tree.
    """
    return find_largest_bst(root)[2]


if __name__ == "__main__":
    root = BinaryTreeNode(50)

    root.left_child = BinaryTreeNode(75)
    root.right_child = BinaryTreeNode(45)

    root.left_child.left_child = BinaryTreeNode(40)

    largest_bst_size = calculate_largest_bst_size(root)

    print("Size of the largest BST is:", largest_bst_size)
