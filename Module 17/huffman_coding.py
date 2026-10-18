
import heapq


# Class to represent a node in the Huffman tree
class HuffmanNode:
    def __init__(self, frequency, symbol, left=None, right=None):
        self.frequency = frequency
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code_bit = ''

    # Compare nodes based on frequency
    def __lt__(self, other_node):
        return self.frequency < other_node.frequency


# Function to print Huffman codes for all characters
def print_huffman_codes(tree_node, current_code=''):

    # Add the current node's code bit
    updated_code = current_code + str(tree_node.code_bit)

    # Traverse the left subtree
    if tree_node.left:
        print_huffman_codes(tree_node.left, updated_code)

    # Traverse the right subtree
    if tree_node.right:
        print_huffman_codes(tree_node.right, updated_code)

    # Print the code if the node is a leaf node
    if not tree_node.left and not tree_node.right:
        print(f"{tree_node.symbol} -> {updated_code}")


# Characters and their frequencies
characters = ['e', 'b', 'c', 'd', 'a', 'f']
frequencies = [5, 9, 12, 13, 16, 45]

# Min-heap to store Huffman tree nodes
priority_queue = []

# Create a node for each character
for index in range(len(characters)):
    heapq.heappush(
        priority_queue,
        HuffmanNode(frequencies[index], characters[index])
    )

# Build the Huffman tree
while len(priority_queue) > 1:

    # Remove the two nodes with the smallest frequencies
    left_node = heapq.heappop(priority_queue)
    right_node = heapq.heappop(priority_queue)

    # Assign binary bits to the child nodes
    left_node.code_bit = 0
    right_node.code_bit = 1

    # Create a parent node by combining both frequencies
    parent_node = HuffmanNode(
        left_node.frequency + right_node.frequency,
        left_node.symbol + right_node.symbol,
        left_node,
        right_node
    )

    heapq.heappush(priority_queue, parent_node)

# Print the Huffman codes
print("Huffman Codes:")
print_huffman_codes(priority_queue[0])
