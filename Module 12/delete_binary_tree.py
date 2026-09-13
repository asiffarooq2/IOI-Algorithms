class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


def insert_node(root, value):
    """Insert a value into the Binary Search Tree."""

    if root is None:
        return BinaryTreeNode(value)

    if value < root.value:
        root.left_child = insert_node(root.left_child, value)

    elif value > root.value:
        root.right_child = insert_node(root.right_child, value)

    else:
        print(f"Value {value} already exists in the tree.")

    return root


def delete_tree(root):
    """Delete all nodes from the tree."""

    if root is None:
        return

    # Delete the left subtree
    delete_tree(root.left_child)
    root.left_child = None

    # Delete the right subtree
    delete_tree(root.right_child)
    root.right_child = None

    # Remove the node's data
    print(f"Deleting node: {root.value}")
    root.value = None


# Create the Binary Search Tree
root = insert_node(None, 15)

insert_node(root, 10)
insert_node(root, 25)
insert_node(root, 6)
insert_node(root, 14)
insert_node(root, 20)
insert_node(root, 60)

print("Deleting all the elements of the binary tree.")

# Delete the complete tree
delete_tree(root)

# Remove the reference to the root
root = None
