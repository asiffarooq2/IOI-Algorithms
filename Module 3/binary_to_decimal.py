def binary_to_decimal(binary_number):
    decimal_value = 0
    power = 0

    for digit in binary_number[::-1]:
        if digit == '1':
            decimal_value += 2 ** power
        power += 1

    return decimal_value


user_input = input("Enter your Binary: ")

print("Decimal :", binary_to_decimal(user_input))
