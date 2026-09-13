class BinaryTreeNode:
    """Represents a node in a binary tree."""

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


def find_nodes_with_one_child(root, single_child_nodes=None):
    """
    Find all nodes that have exactly one child.
    """

    if single_child_nodes is None:
        single_child_nodes = []

    if root is None:
        return single_child_nodes

    # Check if the node has exactly one child
    has_only_left_child = (
        root.left_child is not None
        and root.right_child is None
    )

    has_only_right_child = (
        root.left_child is None
        and root.right_child is not None
    )

    if has_only_left_child or has_only_right_child:
        single_child_nodes.append(root)

    # Search both subtrees
    find_nodes_with_one_child(
        root.left_child,
        single_child_nodes
    )

    find_nodes_with_one_child(
        root.right_child,
        single_child_nodes
    )

    return single_child_nodes


def find_paths_with_sum_range(
    root,
    minimum_sum,
    maximum_sum,
    current_path=None,
    current_sum=0,
    valid_paths=None
):
    """
    Find all root-to-leaf paths whose sums are within a given range.
    """

    if valid_paths is None:
        valid_paths = []

    if current_path is None:
        current_path = []

    if root is None:
        return valid_paths

    # Add the current node to the path
    current_path.append(root.value)
    current_sum += root.value

    # Check the path when a leaf node is reached
    if root.left_child is None and root.right_child is None:

        if minimum_sum <= current_sum <= maximum_sum:
            valid_paths.append(list(current_path))

    else:
        # Search the left subtree
        find_paths_with_sum_range(
            root.left_child,
            minimum_sum,
            maximum_sum,
            current_path,
            current_sum,
            valid_paths
        )

        # Search the right subtree
        find_paths_with_sum_range(
            root.right_child,
            minimum_sum,
            maximum_sum,
            current_path,
            current_sum,
            valid_paths
        )

    # Backtrack
    current_path.pop()

    return valid_paths


def main():
    # Create the binary tree
    root = BinaryTreeNode(2)

    root.left_child = BinaryTreeNode(3)
    root.right_child = BinaryTreeNode(5)

    root.left_child.left_child = BinaryTreeNode(7)

    root.right_child.left_child = BinaryTreeNode(8)
    root.right_child.right_child = BinaryTreeNode(6)

    # Find nodes with exactly one child
    single_child_nodes = find_nodes_with_one_child(root)

    if not single_child_nodes:
        print("No nodes have exactly one child.")
    else:
        print("Nodes with exactly one child:")

        for node in single_child_nodes:
            print(node.value, end=" ")

        print()

    # Define the sum range
    minimum_sum = 14
    maximum_sum = 21

    # Find root-to-leaf paths within the sum range
    valid_paths = find_paths_with_sum_range(
        root,
        minimum_sum,
        maximum_sum
    )

    if valid_paths:
        print(
            f"\nRoot-to-leaf paths with sum in range "
            f"[{minimum_sum}, {maximum_sum}]:"
        )

        for path in valid_paths:
            print(" -> ".join(map(str, path)))
    else:
        print(
            f"\nThere are no root-to-leaf paths with sum "
            f"in range [{minimum_sum}, {maximum_sum}]."
        )


if __name__ == "__main__":
    main()
