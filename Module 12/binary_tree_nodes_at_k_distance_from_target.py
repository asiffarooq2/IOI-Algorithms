class BinaryTreeNode:
    """Represents a node in a binary tree."""

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


def print_nodes_downward(root, distance):
    """
    Print all nodes at the given distance below the current node.
    """

    if root is None or distance < 0:
        return

    if distance == 0:
        print(root.value, end=" ")
        return

    print_nodes_downward(root.left_child, distance - 1)
    print_nodes_downward(root.right_child, distance - 1)


def print_nodes_at_distance(root, target_node, distance):
    """
    Print all nodes at the given distance from the target node.

    Returns:
        int: Distance from the current node to the target node,
             or -1 if the target is not found.
    """

    if root is None:
        return -1

    # Target node found
    if root == target_node:
        print(
            f"Nodes at distance {distance} "
            f"from target {target_node.value}:"
        )

        print_nodes_downward(root, distance)
        return 0

    # Search for the target in the left subtree
    left_distance = print_nodes_at_distance(
        root.left_child,
        target_node,
        distance
    )

    if left_distance != -1:

        # Current node is exactly distance k from target
        if left_distance + 1 == distance:
            print(root.value, end=" ")

        # Search the opposite subtree
        else:
            remaining_distance = distance - left_distance - 2
            print_nodes_downward(
                root.right_child,
                remaining_distance
            )

        return left_distance + 1

    # Search for the target in the right subtree
    right_distance = print_nodes_at_distance(
        root.right_child,
        target_node,
        distance
    )

    if right_distance != -1:

        # Current node is exactly distance k from target
        if right_distance + 1 == distance:
            print(root.value, end=" ")

        # Search the opposite subtree
        else:
            remaining_distance = distance - right_distance - 2
            print_nodes_downward(
                root.left_child,
                remaining_distance
            )

        return right_distance + 1

    return -1


def main():
    # Create the binary tree
    root = BinaryTreeNode(20)

    root.left_child = BinaryTreeNode(8)
    root.right_child = BinaryTreeNode(22)

    root.left_child.left_child = BinaryTreeNode(4)
    root.left_child.right_child = BinaryTreeNode(12)

    root.left_child.right_child.left_child = BinaryTreeNode(10)
    root.left_child.right_child.right_child = BinaryTreeNode(14)

    # Target node is 12
    target_node = root.left_child.right_child

    # Required distance from target
    distance = 2

    print_nodes_at_distance(root, target_node, distance)
    print()


if __name__ == "__main__":
    main()
