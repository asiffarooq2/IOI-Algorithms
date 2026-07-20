number = 16

print("================================")
print("POWER OF TWO SCANNER")
print("================================")

print("\nPART 1: The n & (n-1) Trick")
print("Number      =", number, "->", bin(number))
print("Number - 1  =", number - 1, "->", bin(number - 1))
print("n & (n - 1) =", number & (number - 1), "->", bin(number & (number - 1)))

print("\nThis trick removes the rightmost set bit.")


def is_power_of_two(value):
    return value > 0 and (value & (value - 1)) == 0


print("\nPART 2: Power of 2 Check")

test_numbers = [1, 2, 4, 6, 8, 12, 16, 18, 32]

for value in test_numbers:
    print(value, "->", bin(value), "->", is_power_of_two(value))


def is_power_of_four(value):
    if not is_power_of_two(value):
        return False

    bit_position = 0

    while value > 1:
        value >>= 1
        bit_position += 1

    return bit_position % 2 == 0


print("\nPART 3: Power of 4 Check")

for value in test_numbers:
    print(value, "->", is_power_of_four(value))


def is_power_of_eight(value):
    if not is_power_of_two(value):
        return False

    bit_position = 0

    while value > 1:
        value >>= 1
        bit_position += 1

    return bit_position % 3 == 0


print("\nPART 4: Power of 8 Check")

for value in test_numbers:
    print(value, "->", is_power_of_eight(value))


def binary_exponentiation(base, exponent):
    result = 1

    while exponent > 0:
        if exponent & 1:
            result *= base

        base *= base
        exponent >>= 1

    return result


print("\nPART 5: Binary Exponentiation")
print("2^5 =", binary_exponentiation(2, 5))
print("3^4 =", binary_exponentiation(3, 4))
print("5^3 =", binary_exponentiation(5, 3))

print("\n================================")
print("POWER SCANNER SUMMARY")
print("================================")
print("Power of 2: Only one bit is set.")
print("Power of 4: Set-bit position is even.")
print("Power of 8: Set-bit position is divisible by 3.")
print("Binary exponentiation calculates powers quickly.")
print("================================")
