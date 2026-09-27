# Python program to demonstrate
# insertion operation in Binary Search Tree


# A class representing a node in BST
class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


# Function to insert a new value into BST
def insert_node(root, value):

    # If the tree is empty, create a new node
    if root is None:
        return TreeNode(value)

    # If value already exists, do nothing
    if root.value == value:
        return root

    # If value is greater, insert into right subtree
    elif root.value < value:
        root.right = insert_node(root.right, value)

    # If value is smaller, insert into left subtree
    else:
        root.left = insert_node(root.left, value)

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


# Main program
if __name__ == "__main__":

    # Creating the following BST
    #
    #          50
    #        /    \
    #       30     70
    #      /  \   /  \
    #     20  40 60  80

    root = TreeNode(50)

    # Insert values into the BST
    root = insert_node(root, 30)
    root = insert_node(root, 20)
    root = insert_node(root, 40)
    root = insert_node(root, 70)
    root = insert_node(root, 60)
    root = insert_node(root, 80)

    # Print inorder traversal
    inorder_traversal(root)
