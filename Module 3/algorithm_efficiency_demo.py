rounds = 4

print("=== Counting Game Points (n =", rounds, "rounds) ===")
print()

result = rounds * (rounds + 1) // 2
print("Formula way : total =", result, "| steps = 1")

result = 0
loop_count = 0

for current_round in range(1, rounds + 1):
    result += current_round
    loop_count += 1

print("Loop way    : total =", result, "| steps =", loop_count)

result = 0
operation_count = 0

for current_round in range(1, rounds + 1):
    for current_point in range(1, current_round + 1):
        result += 1
        operation_count += 1

print("Nested loop : total =", result, "| steps =", operation_count)

rounds = 10
nested_operations = 0

for current_round in range(1, rounds + 1):
    for current_point in range(1, current_round + 1):
        nested_operations += 1

print()
print("=== Now with n =", rounds, "rounds ===")
print("Formula way : steps = 1        (always just 1!)")
print("Loop way    : steps =", rounds)
print("Nested loop : steps =", nested_operations, "(grows much faster!)")
print()
print("Same answer — but very different costs. That is time complexity!")