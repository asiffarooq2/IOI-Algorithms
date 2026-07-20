number = 12

print("=== Power Surge ===")
print("Number      =", number, "->", bin(number))
print("Number - 1  =", number - 1, "->", bin(number - 1))
print("n & (n - 1) =", number & (number - 1), "->", bin(number & (number - 1)))
print()

print("Power of 2 Check:")

for value in [1, 4, 6, 16, 18, 64]:
    is_power_of_two = value > 0 and (value & (value - 1)) == 0
    print(value, "->", bin(value), "->", is_power_of_two)

print()


def is_power_of_four(value):
    if value <= 0 or value & (value - 1) != 0:
        return False

    shift_count = 0

    while value > 1:
        value >>= 1
        shift_count += 1

    return shift_count % 2 == 0


print("Power of 4 Check:")

for value in [1, 4, 8, 16, 32, 64]:
    print(value, "->", is_power_of_four(value))

print()


def is_power_of_eight(value):
    if value <= 0 or value & (value - 1) != 0:
        return False

    shift_count = 0

    while value > 1:
        value >>= 1
        shift_count += 1

    return shift_count % 3 == 0


print("Power of 8 Check:")

for value in [1, 8, 16, 64, 32, 512]:
    print(value, "->", is_power_of_eight(value))

print()


def binary_exponentiation(base, exponent):
    result = 1

    while exponent > 0:
        if exponent & 1:
            result *= base

        base *= base
        exponent >>= 1

    return result


print("Binary Exponentiation:")
print("6 ^ 5  =", binary_exponentiation(6, 5))
print("2 ^ 10 =", binary_exponentiation(2, 10))
print("3 ^ 8  =", binary_exponentiation(3, 8))
