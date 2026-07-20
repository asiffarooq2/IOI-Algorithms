first_value = 7
second_value = 7

print("=== Odd Hunt ===")
print("a ^ a =", first_value ^ first_value)
print("a ^ 0 =", first_value ^ 0)
print("Equal (XOR):", (first_value ^ second_value) == 0)
print()

number_list = [3, 5, 3, 5, 9]
xor_result = 0

for number in number_list:
    xor_result ^= number

print("XOR of", number_list, "=", xor_result)
print()

values = [4, 7, 4, 2, 7, 2, 9]
odd_occurring = 0

for number in values:
    odd_occurring ^= number

print("Odd occurring number:", odd_occurring)
print()

pair_values = [3, 9, 3, 5, 5, 7]
combined_xor = 0

for number in pair_values:
    combined_xor ^= number

print("XOR of two odd-occurring numbers:",
      combined_xor, "->", bin(combined_xor))
print()

rightmost_set_bit = combined_xor & -combined_xor

first_odd = 0
second_odd = 0

for number in pair_values:
    if number & rightmost_set_bit:
        first_odd ^= number
    else:
        second_odd ^= number

print("Two odd-occurring numbers:", first_odd, "and", second_odd)
