class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert(self, value):
        """Insert a value into the Binary Search Tree."""

        if value < self.value:
            if self.left_child is None:
                self.left_child = BinaryTreeNode(value)
                print(f"Inserted {value} to the left of {self.value}")
            else:
                self.left_child.insert(value)

        elif value > self.value:
            if self.right_child is None:
                self.right_child = BinaryTreeNode(value)
                print(f"Inserted {value} to the right of {self.value}")
            else:
                self.right_child.insert(value)

        else:
            print(f"Value {value} already exists in the tree.")

    def search(self, target_value):
        """Search for a value in the Binary Search Tree."""

        if self.value == target_value:
            print(f"Found {target_value}")
            return True

        if target_value < self.value:
            if self.left_child is not None:
                return self.left_child.search(target_value)
        else:
            if self.right_child is not None:
                return self.right_child.search(target_value)

        print(f"Value {target_value} not found in the tree.")
        return False


# Create the Binary Search Tree
if __name__ == "__main__":
    root = BinaryTreeNode(13)

    root.insert(10)
    root.insert(25)
    root.insert(6)
    root.insert(14)
    root.insert(20)
    root.insert(60)

    print("\nSearching for values:")

    root.search(14)
    root.search(99)
    root.search(6)
    root.search(88)
