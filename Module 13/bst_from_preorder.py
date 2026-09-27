# Python program to construct
# BST from preorder traversal

# Define a binary tree node
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Function to get the current preorder index
def get_preorder_index():
    return build_bst_from_preorder.preorder_index


# Function to increment the preorder index
def increase_preorder_index():
    build_bst_from_preorder.preorder_index += 1


# Recursive function to construct BST
def build_bst_from_preorder(preorder, start, end):

    # Base case
    if start > end:
        return None

    # The first element in preorder is the root
    root = TreeNode(preorder[get_preorder_index()])

    # Move to the next element
    increase_preorder_index()

    # If there is only one element
    if start == end:
        return root

    # Find the first element greater than the root
    right_subtree_index = -1

    for index in range(start, end + 1):
        if preorder[index] > root.value:
            right_subtree_index = index
            break

    # If no greater element is found,
    # all remaining elements belong to the left subtree
    if right_subtree_index == -1:
        right_subtree_index = (
            get_preorder_index() + (end - start)
        )

    # Construct the left subtree
    root.left = build_bst_from_preorder(
        preorder,
        get_preorder_index(),
        right_subtree_index - 1
    )

    # Construct the right subtree
    root.right = build_bst_from_preorder(
        preorder,
        right_subtree_index,
        end
    )

    return root


# Main function to construct BST
def create_bst(preorder):
    total_elements = len(preorder)

    # Start from the first element
    build_bst_from_preorder.preorder_index = 0

    return build_bst_from_preorder(
        preorder,
        0,
        total_elements - 1
    )


# Function to perform inorder traversal
def inorder_traversal(root):

    if root is None:
        return

    inorder_traversal(root.left)

    print(root.value, end=" ")

    inorder_traversal(root.right)


# Preorder traversal
preorder = [10, 5, 1, 7, 40, 50]

# Create BST
root = create_bst(preorder)

# Print inorder traversal
inorder_traversal(root)
