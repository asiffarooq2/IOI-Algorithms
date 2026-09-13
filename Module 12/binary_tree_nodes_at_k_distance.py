class BinaryTreeNode:
    """Represents a node in a binary tree."""

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


def print_nodes_at_distance(root, distance):
    """
    Print all nodes that are at a given distance from the root.
    """

    if root is None:
        return

    # Distance 0 means the current node
    if distance == 0:
        print(root.value, end=" ")
        return

    # Search the left and right subtrees
    print_nodes_at_distance(root.left_child, distance - 1)
    print_nodes_at_distance(root.right_child, distance - 1)


def main():
    # Create the binary tree
    root = BinaryTreeNode(1)

    root.left_child = BinaryTreeNode(2)
    root.right_child = BinaryTreeNode(3)

    root.left_child.left_child = BinaryTreeNode(4)
    root.left_child.right_child = BinaryTreeNode(5)

    root.right_child.left_child = BinaryTreeNode(8)

    # Distance from the root
    distance = 2

    print(f"Nodes at distance {distance} from root:")
    print_nodes_at_distance(root, distance)
    print()


if __name__ == "__main__":
    main()
