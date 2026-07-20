number = 52


def binary_format(value):
    return bin(value)[2:]


print("=== Bit Play ===")
print("Number =", number, "->", binary_format(number))
print("Set bits (1s):", binary_format(number).count("1"))
print("Zero bits (0s):", binary_format(number).count("0"))
print()

set_bit_count = 0
current_value = number

while current_value:
    if current_value & 1:
        set_bit_count += 1
    current_value >>= 1

print("Set bits in", number, ":", set_bit_count)
print()

first_set_position = 1
current_value = number

while current_value:
    if current_value & 1:
        break
    first_set_position += 1
    current_value >>= 1

print("First set bit of", number, "-> Position", first_set_position)
print()

print("Bit Masks (1 << i):")

for shift_value in range(6):
    mask = 1 << shift_value
    print(f"1 << {shift_value} = {mask:2d} -> {binary_format(mask)}")

print()

print("Bits of", number, "->", binary_format(number) + ":")

for bit_position in range(1, 7):
    status = "SET" if number & (1 << (bit_position - 1)) else "NOT SET"
    print(f"Bit {bit_position}: {status}")
