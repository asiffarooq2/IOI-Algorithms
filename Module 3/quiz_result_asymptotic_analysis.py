scores = [45, 62, 78, 85, 91, 56, 73, 88]

print("================================")
print("MY QUIZ RESULT SEARCHER")
print("================================")
print("Quiz Scores:", scores)

first_result = scores[0]

print()
print("PART 1: Direct Access")
print("First Student Score:", first_result)
print("Time Complexity: O(1)")
print("Theta Notation: Theta(1)")
print("Reason: Direct access takes one step.")

search_value = 88
step_count = 0
is_found = False

print()
print("PART 2: Linear Search")
print("Searching for score:", search_value)

for current_score in scores:
    step_count += 1

    if current_score == search_value:
        is_found = True
        print("Score found:", current_score)
        print("Steps Taken:", step_count)
        break

if not is_found:
    print("Score not found.")
    print("Steps Taken:", step_count)

print("Best Case: Omega(1)")
print("Average Case: O(n)")
print("Worst Case: O(n)")
print("Reason: The program may need to check many scores.")

print()
print("PART 3: Pair Comparison")

comparison_count = 0

for first_score in scores:
    for second_score in scores:
        comparison_count += 1

print("Total Pair Checks:", comparison_count)
print("Time Complexity: O(n²)")
print("Reason: A nested loop compares every score with every other score.")

print()
print("PART 4: Case Comparison")

best_target = 45
middle_target = 85
last_target = 88

print("Best Case Target:", best_target, "- Found near the beginning")
print("Average Case Target:", middle_target, "- Found around the middle")
print("Worst Case Target:", last_target, "- Found near the end")

print()
print("================================")
print("ASYMPTOTIC ANALYSIS SUMMARY")
print("================================")
print("O(1): Direct access is fastest.")
print("O(n): Linear search grows with the number of scores.")
print("O(n²): Nested loops grow much faster.")
print("Omega(1): Best case for search when the target is found first.")
print("Theta(1): Direct access always takes constant time.")
print("Big-O shows the upper/worst-case growth.")
print("================================")
