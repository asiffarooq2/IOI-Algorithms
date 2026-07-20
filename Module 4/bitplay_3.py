first_number = 56
second_number = 12

print("=== Bitplay 3 ===")
print("Before Swap: First Number =", first_number,
      "Second Number =", second_number)

first_number = first_number + second_number
second_number = first_number - second_number
first_number = first_number - second_number

print("After Arithmetic Swap: First Number =",
      first_number, "Second Number =", second_number)
print()

first_number = 56
second_number = 12

first_number ^= second_number
second_number ^= first_number
first_number ^= second_number

print("After XOR Swap: First Number =",
      first_number, "Second Number =", second_number)
print()

print("Left Shift Results:")
print("3 << 1 =", 3 << 1)
print("3 << 2 =", 3 << 2)
print("3 << 3 =", 3 << 3)
print("3 << 4 =", 3 << 4)
print("3 << 5 =", 3 << 5)
print()


def divide_without_operator(dividend, divisor):
    is_negative = (dividend < 0) ^ (divisor < 0)

    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0

    while dividend >= divisor:
        dividend -= divisor
        quotient += 1

    if is_negative:
        quotient = -quotient

    return quotient


print("Division Without '/' Operator:")
print("50 / 2  =", divide_without_operator(50, 2))
print("72 / 3  =", divide_without_operator(72, 3))
print("-50 / 2 =", divide_without_operator(-50, 2))
print("50 / -2 =", divide_without_operator(50, -2))
