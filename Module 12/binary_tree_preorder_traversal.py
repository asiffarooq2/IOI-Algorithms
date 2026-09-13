from binarytree import build


class BinaryTreeNode:
    """Represents a node in a binary tree."""

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


def print_preorder(root):
    """Perform a pre-order traversal of the binary tree."""

    if root is not None:
        # Visit the current node
        print(root.value, end=" ")

        # Visit the left subtree
        print_preorder(root.left_child)

        # Visit the right subtree
        print_preorder(root.right_child)


if __name__ == "__main__":
    # Create the binary tree
    root = BinaryTreeNode(1)

    root.left_child = BinaryTreeNode(2)
    root.right_child = BinaryTreeNode(3)

    root.left_child.left_child = BinaryTreeNode(4)
    root.left_child.right_child = BinaryTreeNode(5)

    # Create a tree using the binarytree library for visualization
    tree_values = [1, 2, 3, 4, 5]
    visual_tree = build(tree_values)

    print("Binary tree visualization:")
    print(visual_tree)

    # Perform pre-order traversal
    print("Pre-order traversal of binary tree:")
    print_preorder(root)
    print()
