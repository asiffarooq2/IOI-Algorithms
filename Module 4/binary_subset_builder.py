elements = ["A", "B", "C"]

element_count = len(elements)
subset_count = 2 ** element_count

print("================================")
print("BINARY SUBSET BUILDER")
print("================================")

print("Items:", elements)
print("Number of Items:", element_count)
print("Total Subsets: 2 ^", element_count, "=", subset_count)

print("\nPART 1: Power Set")
print("For", element_count, "items, we can create", subset_count, "subsets.")

print("\nPART 2: Binary Mask Table")

current_mask = 0

while current_mask < subset_count:
    bit_c = (current_mask >> 2) & 1
    bit_b = (current_mask >> 1) & 1
    bit_a = current_mask & 1

    print("Mask", current_mask, "-> [C][B][A] =", bit_c, bit_b, bit_a)

    current_mask += 1

print("\nPART 3: Bit Probe")

sample_mask = 5

print("Sample Mask:", sample_mask)
print("Binary:", bin(sample_mask))

bit_position = 0

while bit_position < element_count:
    bit_mask = 1 << bit_position

    if sample_mask & bit_mask:
        print("Bit", bit_position, "is set, so item",
              elements[bit_position], "is selected.")
    else:
        print("Bit", bit_position, "is not set, so item",
              elements[bit_position], "is not selected.")

    bit_position += 1

print("\nPART 4: All Subsets")

current_mask = 0

while current_mask < subset_count:
    current_subset = []

    bit_position = 0

    while bit_position < element_count:
        bit_mask = 1 << bit_position

        if current_mask & bit_mask:
            current_subset.append(elements[bit_position])

        bit_position += 1

    print("Mask", current_mask, "->", current_subset)

    current_mask += 1


def bit_difference(first_number, second_number):
    difference_count = 0

    while first_number > 0 or second_number > 0:
        first_bit = first_number & 1
        second_bit = second_number & 1

        if first_bit != second_bit:
            difference_count += 1

        first_number >>= 1
        second_number >>= 1

    return difference_count


print("\nPART 5: Bit Difference")
print("Difference between 12 and 15:", bit_difference(12, 15))
print("12 =", bin(12), "15 =", bin(15))

print("Difference between 21 and 24:", bit_difference(21, 24))
print("21 =", bin(21), "24 =", bin(24))

print("Difference between 8 and 8:", bit_difference(8, 8))
print("8 =", bin(8), "8 =", bin(8))

print("\n================================")
print("BINARY SUBSET BUILDER SUMMARY")
print("================================")
print("Power Set: All possible subsets of a set.")
print("Binary Mask: A number that selects items using bits.")
print("Bit Probe: Uses 1 << j to check a specific bit.")
print("Two Loops: One loop for masks and one loop for items.")
print("Bit Difference: Counts different bit positions.")
print("================================")
