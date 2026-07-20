marks = [12, 25, 33, 41, 50, 67, 72, 85, 91, 98]

total_scores = len(marks)
search_score = 98

print("=== Quiz Score Finder (n =", total_scores, "scores) ===")
print("Scores:", marks, "| Target:", search_score)
print()

linear_steps = 0

for position in range(total_scores):
    linear_steps += 1
    if marks[position] == search_score:
        print("Linear search  : index =", position,
              "| steps =", linear_steps, "| O(n)")
        break

print()

left = 0
right = total_scores - 1
binary_steps = 0

while left <= right:
    middle = (left + right) // 2
    binary_steps += 1

    if marks[middle] == search_score:
        print("Binary search  : index =", middle,
              "| steps =", binary_steps, "| O(log n)")
        break
    elif marks[middle] < search_score:
        left = middle + 1
    else:
        right = middle - 1

print()


def recursive_search(data, left, right, target_value, call_count=0):
    call_count += 1

    if left > right:
        return -1, call_count

    middle = (left + right) // 2

    if data[middle] == target_value:
        return middle, call_count
    elif data[middle] < target_value:
        return recursive_search(data, middle + 1, right, target_value, call_count)
    else:
        return recursive_search(data, left, middle - 1, target_value, call_count)


found_index, recursive_calls = recursive_search(
    marks, 0, total_scores - 1, search_score
)

print("Recursive search : index =", found_index,
      "| calls =", recursive_calls, "| O(log n)")
print()

print("=== Space and Complexity Summary ===")
print("Iterative : O(1) space  — only left, right, middle")
print("Recursive : O(log n) space —", recursive_calls,
      "stack frames for n =", total_scores)
print()

print("Complexity ladder (n =", total_scores, "):")
print("O(1)     : 1 step   — constant, never grows")
print("O(log n) :", binary_steps, "steps — halving, grows slowly")
print("O(n)     :", total_scores, "steps — linear, grows with n")
print("O(n²)    :", total_scores * total_scores,
      "steps — quadratic, grows fast!")
