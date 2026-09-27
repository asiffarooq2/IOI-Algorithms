# Python program to implement
# inorder traversal of BST

# Define a Node
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Function to create a new BST node
def create_node(value):
    new_node = TreeNode(value)
    return new_node


# Function to insert a new node into BST
def insert_node(root, value):

    # If the tree is empty, create a new node
    if root is None:
        return create_node(value)

    # Insert smaller values into the left subtree
    if value < root.value:
        root.left = insert_node(root.left, value)

    # Insert larger values into the right subtree
    elif value > root.value:
        root.right = insert_node(root.right, value)

    # Return the root node
    return root


# Function to perform inorder traversal
def inorder_traversal(root):

    if root:
        # Visit left subtree
        inorder_traversal(root.left)

        # Visit root
        print(root.value, end=" ")

        # Visit right subtree
        inorder_traversal(root.right)


# Driver Code
if __name__ == "__main__":

    # Creating the following BST
    #
    #          50
    #        /    \
    #       30     70
    #      /  \   /  \
    #     20  40 60  80

    root = None

    # Insert values into the BST
    root = insert_node(root, 50)
    insert_node(root, 30)
    insert_node(root, 20)
    insert_node(root, 40)
    insert_node(root, 70)
    insert_node(root, 60)
    insert_node(root, 80)

    # Perform inorder traversal
    inorder_traversal(root)