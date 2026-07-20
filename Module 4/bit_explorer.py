first_number = 10
second_number = 6


def binary_format(value, width=4):
    return format(value & ((1 << width) - 1), f"0{width}b")


print("=== Bit Explorer ===")
print("First Number =", first_number, "->", binary_format(first_number))
print("Second Number =", second_number, "->", binary_format(second_number))
print()

print("AND  =", first_number & second_number, "->", binary_format(first_number & second_number))
print("OR   =", first_number | second_number, "->", binary_format(first_number | second_number))
print()

print("NOT  =", ~first_number & 0xFF, "->", binary_format(~first_number, 8))
print("XOR  =", first_number ^ second_number, "->", binary_format(first_number ^ second_number))
print()

print("LEFT SHIFT  =", first_number << 1)
print("RIGHT SHIFT =", first_number >> 1)
print()

print("Odd or Even:")

for value in [7, 10, 15, 4]:
    answer = "Even" if value ^ 1 == value + 1 else "Odd"
    print(value, "->", answer)

print()


def bit_length(value):
    total_bits = 0

    while value:
        total_bits += 1
        value >>= 1

    return total_bits


print("Bit Count:")

for value in [first_number, second_number, 255]:
    print(value, "->", bit_length(value), "bits |", binary_format(value, bit_length(value)))