elements = ["A", "B", "C"]

element_count = len(elements)
total_subsets = 2 ** element_count

print("=== Power Map ===")
print("Items:", elements)
print("Elements:", element_count, " Total Subsets: 2 ^",
      element_count, "=", total_subsets)
print()

print("Binary Mask Table:")

current_mask = 0

while current_mask < total_subsets:
    bit_c = (current_mask >> 2) & 1
    bit_b = (current_mask >> 1) & 1
    bit_a = current_mask & 1

    print("Mask", current_mask, "-> [C][B][A] =", bit_c, bit_b, bit_a)

    current_mask += 1

print()

print("All Subsets:")

current_mask = 0

while current_mask < total_subsets:
    current_subset = []
    position = 0

    while position < element_count:
        bit_mask = 1 << position

        if current_mask & bit_mask:
            current_subset.append(elements[position])

        position += 1

    print("Mask", current_mask, "->", current_subset)

    current_mask += 1

print()


def bit_difference(first_number, second_number):
    different_bits = 0

    while first_number > 0 or second_number > 0:
        first_bit = first_number & 1
        second_bit = second_number & 1

        if first_bit != second_bit:
            different_bits += 1

        first_number >>= 1
        second_number >>= 1

    return different_bits


print("Bit Difference:")
print("diff(12, 15) =", bit_difference(12, 15), "(12 = 1100, 15 = 1111)")
print("diff(21, 24) =", bit_difference(21, 24), "(21 = 10101, 24 = 11000)")
print("diff(8, 8)   =", bit_difference(8, 8), "(Same -> 0)")
