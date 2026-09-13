# Python program to implement a Binary Tree using an Array


# Create an array to store the binary tree
tree_array = [None] * 10


# Ensure that the array has enough space
def ensure_capacity(child_index):
    if child_index >= len(tree_array):

        # Double the array size when required
        new_size = max(child_index + 1, len(tree_array) * 2)

        tree_array.extend(
            [None] * (new_size - len(tree_array))
        )


# Set the root node
def set_root(value):
    if tree_array[0] is not None:
        print("Tree already has a root.")
    else:
        tree_array[0] = value


# Set the left child of a parent node
def set_left_child(value, parent_index):

    child_index = (parent_index * 2) + 1

    # Check whether the parent exists
    if (
        parent_index >= len(tree_array)
        or tree_array[parent_index] is None
    ):
        print(
            f"Cannot set left child at index {child_index}. "
            f"No parent found at index {parent_index}."
        )
    else:
        ensure_capacity(child_index)
        tree_array[child_index] = value


# Set the right child of a parent node
def set_right_child(value, parent_index):

    child_index = (parent_index * 2) + 2

    # Check whether the parent exists
    if (
        parent_index >= len(tree_array)
        or tree_array[parent_index] is None
    ):
        print(
            f"Cannot set right child at index {child_index}. "
            f"No parent found at index {parent_index}."
        )
    else:
        ensure_capacity(child_index)
        tree_array[child_index] = value


# Print the binary tree array
def display_tree_array():
    print("Binary Tree Array:")

    for index, value in enumerate(tree_array):
        if value is not None:
            print(value, end=" ")
        else:
            print("-", end=" ")

    print()


# Display the tree visually
def display_tree_visual(index, indentation=0):

    # Check whether the index contains a node
    if (
        index < len(tree_array)
        and tree_array[index] is not None
    ):

        # Display the right subtree first
        display_tree_visual(
            (index * 2) + 2,
            indentation + 4
        )

        # Display the current node
        print(
            " " * indentation
            + str(tree_array[index])
        )

        # Display the left subtree
        display_tree_visual(
            (index * 2) + 1,
            indentation + 4
        )


# Main program

set_root("A")

set_left_child("B", 0)
set_right_child("C", 0)

set_left_child("D", 1)
set_right_child("E", 1)

set_left_child("F", 2)
set_right_child("G", 2)

set_left_child("H", 3)
set_right_child("I", 3)


# Display the tree as an array
display_tree_array()


# Display the tree visually
print("\nVisual Representation of the Binary Tree:")
display_tree_visual(0)
