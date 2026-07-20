laps = 5

print("================================")
print("MY RUNNING LAP TRACKER")
print("================================")
print("Number of laps:", laps)
print()

total_points = laps * (laps + 1) // 2

print("Solution 1: Formula Method")
print("Total Running Points:", total_points)
print("Time Complexity: O(1)")
print("Space Complexity: O(1)")
print()

sum_points = 0
loop_steps = 0

for current_lap in range(1, laps + 1):
    sum_points += current_lap
    loop_steps += 1

print("Solution 2: Loop Method")
print("Total Running Points:", sum_points)
print("Steps Taken:", loop_steps)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")
print()

count_points = 0
nested_steps = 0

for current_lap in range(1, laps + 1):
    for lap_point in range(1, current_lap + 1):
        count_points += 1
        nested_steps += 1

print("Solution 3: Nested Loop Method")
print("Total Running Points:", count_points)
print("Steps Taken:", nested_steps)
print("Time Complexity: O(n²)")
print("Space Complexity: O(1)")
print()

print("================================")
print("ALGORITHM EFFICIENCY COMPARISON")
print("================================")
print("Formula Method: Fastest because it uses only one calculation.")
print("Loop Method: Slower because it repeats once for every lap.")
print("Nested Loop Method: Slowest because it uses one loop inside another.")
print()
print("Best Method: Formula Method")
print("Reason: It has O(1) time complexity, so it remains fast even for a large number of laps.")
print("================================")
