seat_list = [101, 104, 108, 112, 115, 120, 125, 130, 135, 140, 145, 150]
seat_to_find = 130

print("================================")
print("MY TRAIN SEAT FINDER")
print("================================")
print("Available Seats:", seat_list)
print("Seat to Find:", seat_to_find)


def find_seat(data, target):
    left = 0
    right = len(data) - 1
    step_count = 0

    while left <= right:
        step_count += 1
        middle = (left + right) // 2
        print("Checking middle seat:", data[middle])

        if data[middle] == target:
            return middle, step_count
        elif target < data[middle]:
            right = middle - 1
        else:
            left = middle + 1

    return -1, step_count


seat_index, total_steps = find_seat(seat_list, seat_to_find)

print()
print("Binary Search Result:")

if seat_index != -1:
    print("Seat found at index:", seat_index)
else:
    print("Seat not found.")

print("Steps Taken:", total_steps)
print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")


def recursive_find(data, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2
    print("Recursive check:", data[middle])

    if data[middle] == target:
        return middle
    elif target < data[middle]:
        return recursive_find(data, target, left, middle - 1)
    else:
        return recursive_find(data, target, middle + 1, right)


recursive_result = recursive_find(
    seat_list,
    seat_to_find,
    0,
    len(seat_list) - 1
)

print()
print("Recursive Binary Search Result:")

if recursive_result != -1:
    print("Seat found at index:", recursive_result)
else:
    print("Seat not found.")

print("Recursive Time Complexity: O(log n)")
print("Space Complexity: O(log n) because of the call stack")

print()
print("================================")
print("COMPLEXITY LADDER")
print("================================")
print("O(1): Directly checking one fixed seat")
print("O(log n): Binary search by cutting the list in half")
print("O(n): Checking every seat one by one")
print("O(n²): Comparing every seat with every other seat")
print("================================")

print()
print("SUMMARY")
print("Binary search is faster than checking every seat one by one.")
print("It works only when the seat list is sorted.")
print("Recursive binary search also uses O(log n) time.")
print("However, recursion uses extra space in the call stack.")
