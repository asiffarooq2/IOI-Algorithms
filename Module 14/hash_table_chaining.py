# Python program to implement
# Hash Table using Separate Chaining


# Class representing a node in the linked list
class HashNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_node = None


# Class representing the Hash Table
class HashTable:

    def __init__(self, capacity):

        # Maximum number of buckets
        self.capacity = capacity

        # Number of key-value pairs
        self.size = 0

        # Create empty hash table
        self.buckets = [None] * capacity

    # Function to calculate hash index

    def get_hash_index(self, key):

        return hash(key) % self.capacity

    # Function to insert a key-value pair

    def insert(self, key, value):

        # Find the bucket index
        bucket_index = self.get_hash_index(key)

        # If bucket is empty
        if self.buckets[bucket_index] is None:

            self.buckets[bucket_index] = HashNode(
                key,
                value
            )

            self.size += 1

        else:

            # Traverse the linked list
            current_node = self.buckets[bucket_index]

            while current_node:

                # If key already exists,
                # update its value
                if current_node.key == key:

                    current_node.value = value
                    return

                current_node = current_node.next_node

            # Key does not exist,
            # create a new node
            new_node = HashNode(
                key,
                value
            )

            # Add new node at the beginning
            new_node.next_node = (
                self.buckets[bucket_index]
            )

            self.buckets[bucket_index] = new_node

            self.size += 1

    # Function to search for a key

    def search(self, key):

        # Find bucket index
        bucket_index = self.get_hash_index(key)

        # Start from first node
        current_node = self.buckets[bucket_index]

        # Search through linked list
        while current_node:

            if current_node.key == key:
                return current_node.value

            current_node = current_node.next_node

        # Key was not found
        raise KeyError(key)

    # Function to remove a key-value pair

    def remove(self, key):

        # Find bucket index
        bucket_index = self.get_hash_index(key)

        previous_node = None
        current_node = self.buckets[bucket_index]

        # Search for the key
        while current_node:

            if current_node.key == key:

                # If node is not the first node
                if previous_node:

                    previous_node.next_node = (
                        current_node.next_node
                    )

                # If node is the first node
                else:

                    self.buckets[bucket_index] = (
                        current_node.next_node
                    )

                self.size -= 1
                return

            previous_node = current_node
            current_node = current_node.next_node

        # Key was not found
        raise KeyError(key)

    # Function to return number of elements

    def __len__(self):

        return self.size

    # Function to check whether a key exists

    def __contains__(self, key):

        try:

            self.search(key)
            return True

        except KeyError:

            return False


# Main program
if __name__ == "__main__":

    # Create a hash table with capacity 5
    hash_table = HashTable(5)

    # Insert key-value pairs
    hash_table.insert("apple", 3)
    hash_table.insert("banana", 2)
    hash_table.insert("cherry", 5)

    # Check whether keys exist
    print("apple" in hash_table)
    print("durian" in hash_table)

    # Search for a key
    print(hash_table.search("banana"))

    # Update the value
    hash_table.insert("banana", 4)

    print(hash_table.search("banana"))

    # Remove a key
    hash_table.remove("apple")

    print("apple" in hash_table)
