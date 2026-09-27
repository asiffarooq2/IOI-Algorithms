# Python program to demonstrate
# Segment Tree construction, query, and update

from math import ceil, log2


# Function to find the middle index
def find_middle(start, end):
    return start + (end - start) // 2


# Function to calculate the sum of a given range
def range_sum_util(
    segment_tree,
    segment_start,
    segment_end,
    query_start,
    query_end,
    tree_index
):

    # Case 1: Current segment is completely
    # inside the query range
    if query_start <= segment_start and query_end >= segment_end:
        return segment_tree[tree_index]

    # Case 2: Current segment is completely
    # outside the query range
    if segment_end < query_start or segment_start > query_end:
        return 0

    # Case 3: Current segment partially overlaps
    # with the query range
    middle = find_middle(segment_start, segment_end)

    left_sum = range_sum_util(
        segment_tree,
        segment_start,
        middle,
        query_start,
        query_end,
        2 * tree_index + 1
    )

    right_sum = range_sum_util(
        segment_tree,
        middle + 1,
        segment_end,
        query_start,
        query_end,
        2 * tree_index + 2
    )

    return left_sum + right_sum


# Function to update values in the segment tree
def update_value_util(
    segment_tree,
    segment_start,
    segment_end,
    array_index,
    difference,
    tree_index
):

    # If index is outside the current segment
    if array_index < segment_start or array_index > segment_end:
        return

    # Update the current segment
    segment_tree[tree_index] += difference

    # If this is not a leaf node,
    # update its child nodes
    if segment_start != segment_end:

        middle = find_middle(segment_start, segment_end)

        # Update left subtree
        update_value_util(
            segment_tree,
            segment_start,
            middle,
            array_index,
            difference,
            2 * tree_index + 1
        )

        # Update right subtree
        update_value_util(
            segment_tree,
            middle + 1,
            segment_end,
            array_index,
            difference,
            2 * tree_index + 2
        )


# Function to update an array value
def update_value(array, segment_tree, size, array_index, new_value):

    # Check for invalid index
    if array_index < 0 or array_index > size - 1:
        print("Invalid Input")
        return

    # Calculate the difference
    difference = new_value - array[array_index]

    # Update the original array
    array[array_index] = new_value

    # Update the segment tree
    update_value_util(
        segment_tree,
        0,
        size - 1,
        array_index,
        difference,
        0
    )


# Function to calculate sum of a range
def get_range_sum(
    segment_tree,
    size,
    query_start,
    query_end
):

    # Check for invalid range
    if (
        query_start < 0
        or query_end > size - 1
        or query_start > query_end
    ):
        print("Invalid Input")
        return -1

    return range_sum_util(
        segment_tree,
        0,
        size - 1,
        query_start,
        query_end,
        0
    )


# Recursive function to construct
# the Segment Tree
def build_segment_tree_util(
    array,
    segment_start,
    segment_end,
    segment_tree,
    tree_index
):

    # If there is only one element,
    # store it in the current tree node
    if segment_start == segment_end:

        segment_tree[tree_index] = array[segment_start]

        return array[segment_start]

    # Find the middle index
    middle = find_middle(segment_start, segment_end)

    # Build the left subtree
    left_sum = build_segment_tree_util(
        array,
        segment_start,
        middle,
        segment_tree,
        2 * tree_index + 1
    )

    # Build the right subtree
    right_sum = build_segment_tree_util(
        array,
        middle + 1,
        segment_end,
        segment_tree,
        2 * tree_index + 2
    )

    # Store the sum of both subtrees
    segment_tree[tree_index] = left_sum + right_sum

    return segment_tree[tree_index]


# Function to construct the Segment Tree
def build_segment_tree(array):

    size = len(array)

    # Calculate the height of the tree
    tree_height = int(ceil(log2(size)))

    # Calculate maximum required size
    max_size = 2 * (2 ** tree_height) - 1

    # Create an empty segment tree
    segment_tree = [0] * max_size

    # Build the segment tree
    build_segment_tree_util(
        array,
        0,
        size - 1,
        segment_tree,
        0
    )

    return segment_tree


# Main program
if __name__ == "__main__":

    # Given array
    array = [1, 3, 5, 7, 9, 11]

    size = len(array)

    # Build the Segment Tree
    segment_tree = build_segment_tree(array)

    # Find sum from index 1 to 3
    print(
        "Sum of values in given range =",
        get_range_sum(segment_tree, size, 1, 3)
    )

    # Update array[1] from 3 to 10
    update_value(
        array,
        segment_tree,
        size,
        1,
        10
    )

    # Find sum again after update
    print(
        "Updated sum of values in given range =",
        get_range_sum(segment_tree, size, 1, 3)
    )
