# Python program to implement
# B-Tree insertion and search operations


# Class representing a node in B-Tree
class BTreeNode:

    def __init__(self, is_leaf=False):
        self.is_leaf = is_leaf      # True if node is a leaf
        self.keys = []              # Stores keys
        self.children = []          # Stores child nodes


# Class representing the B-Tree
class BTree:

    def __init__(self, minimum_degree):
        # Initially, root is a leaf node
        self.root = BTreeNode(is_leaf=True)

        # Minimum degree of B-Tree
        self.minimum_degree = minimum_degree

    # Function to insert a key into the B-Tree

    def insert(self, key):

        root = self.root

        # Check if root is full
        if len(root.keys) == (2 * self.minimum_degree) - 1:

            # Create a new root
            new_root = BTreeNode()

            self.root = new_root

            # Old root becomes child of new root
            new_root.children.insert(0, root)

            # Split the old root
            self.split_child(new_root, 0)

            # Insert key into the new root
            self.insert_into_non_full(new_root, key)

        else:

            # Root is not full
            self.insert_into_non_full(root, key)

    # Function to insert a key into a non-full node

    def insert_into_non_full(self, current_node, key):

        index = len(current_node.keys) - 1

        # If current node is a leaf
        if current_node.is_leaf:

            # Add an empty position
            current_node.keys.append((None, None))

            # Move larger keys one position to the right
            while (
                index >= 0
                and key[0] < current_node.keys[index][0]
            ):
                current_node.keys[index + 1] = current_node.keys[index]
                index -= 1

            # Insert the new key
            current_node.keys[index + 1] = key

        else:

            # Find the correct child
            while (
                index >= 0
                and key[0] < current_node.keys[index][0]
            ):
                index -= 1

            index += 1

            # If child is full, split it
            if (
                len(current_node.children[index].keys)
                == (2 * self.minimum_degree) - 1
            ):

                self.split_child(current_node, index)

                # Decide which child should receive the key
                if key[0] > current_node.keys[index][0]:
                    index += 1

            # Insert key into the selected child
            self.insert_into_non_full(
                current_node.children[index],
                key
            )

    # Function to split a full child

    def split_child(self, parent_node, child_index):

        degree = self.minimum_degree

        # Get the full child
        full_child = parent_node.children[child_index]

        # Create a new node
        new_child = BTreeNode(full_child.is_leaf)

        # Add the new child
        parent_node.children.insert(
            child_index + 1,
            new_child
        )

        # Move the middle key to the parent
        parent_node.keys.insert(
            child_index,
            full_child.keys[degree - 1]
        )

        # Copy the last keys to the new child
        new_child.keys = full_child.keys[
            degree:(2 * degree) - 1
        ]

        # Keep the first keys in the original child
        full_child.keys = full_child.keys[
            0:degree - 1
        ]

        # If the child is not a leaf,
        # move its children as well
        if not full_child.is_leaf:

            new_child.children = full_child.children[
                degree:2 * degree
            ]

            full_child.children = full_child.children[
                0:degree
            ]

    # Function to print the B-Tree

    def print_tree(self, current_node, level=0):

        print(
            "Level",
            level,
            ":",
            len(current_node.keys),
            "keys ->",
            end=" "
        )

        for key in current_node.keys:
            print(key, end=" ")

        print()

        # Print child nodes
        if len(current_node.children) > 0:

            for child_node in current_node.children:

                self.print_tree(
                    child_node,
                    level + 1
                )

    # Function to search for a key

    def search_key(self, target_key, current_node=None):

        # Start searching from root
        if current_node is None:
            current_node = self.root

        index = 0

        # Find the possible position of the key
        while (
            index < len(current_node.keys)
            and target_key > current_node.keys[index][0]
        ):
            index += 1

        # Key found
        if (
            index < len(current_node.keys)
            and target_key == current_node.keys[index][0]
        ):
            return (current_node, index)

        # Key not found in a leaf
        elif current_node.is_leaf:
            return None

        # Search in the appropriate child
        else:
            return self.search_key(
                target_key,
                current_node.children[index]
            )


# Main function
def main():

    # Create a B-Tree with minimum degree 3
    btree = BTree(3)

    # Insert keys into the B-Tree
    for number in range(10):

        # Store key-value pair
        btree.insert(
            (number, 2 * number)
        )

    # Display the B-Tree
    print("B-Tree structure:")
    btree.print_tree(btree.root)

    # Search for key 8
    search_result = btree.search_key(8)

    if search_result is not None:
        print("\nKey 8 Found")
    else:
        print("\nKey 8 Not Found")


# Start the program
if __name__ == "__main__":
    main()
