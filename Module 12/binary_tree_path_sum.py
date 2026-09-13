class BinaryTreeNode:
    """Represents a node in a binary tree."""

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


def has_root_to_leaf_sum(root, target_sum):
    """
    Check whether a root-to-leaf path has the given sum.
    """

    if root is None:
        return False

    remaining_sum = target_sum - root.value

    # Check whether the current node is a leaf
    if root.left_child is None and root.right_child is None:
        return remaining_sum == 0

    # Search both subtrees
    return (
        has_root_to_leaf_sum(root.left_child, remaining_sum)
        or has_root_to_leaf_sum(root.right_child, remaining_sum)
    )


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

    # Check the path when we reach a leaf node
    if root.left_child is None and root.right_child is None:

        if minimum_sum <= current_sum <= maximum_sum:
            valid_paths.append(list(current_path))

    else:
        # Continue searching both subtrees
        find_paths_with_sum_range(
            root.left_child,
            minimum_sum,
            maximum_sum,
            current_path,
            current_sum,
            valid_paths
        )

        find_paths_with_sum_range(
            root.right_child,
            minimum_sum,
            maximum_sum,
            current_path,
            current_sum,
            valid_paths
        )

    # Backtrack before returning
    current_path.pop()

    return valid_paths


def main():
    # Target sum for the existence check
    target_sum = 21

    # Create the binary tree
    root = BinaryTreeNode(10)

    root.left_child = BinaryTreeNode(8)
    root.right_child = BinaryTreeNode(2)

    root.left_child.left_child = BinaryTreeNode(3)
    root.left_child.right_child = BinaryTreeNode(5)

    root.right_child.left_child = BinaryTreeNode(2)

    # Check for a root-to-leaf path with the target sum
    if has_root_to_leaf_sum(root, target_sum):
        print(
            f"There is at least one root-to-leaf path "
            f"with sum {target_sum}."
        )
    else:
        print(
            f"There is no root-to-leaf path "
            f"with sum {target_sum}."
        )

    # Define the sum range
    minimum_sum = 14
    maximum_sum = 21

    # Find all paths within the given sum range
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
