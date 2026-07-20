def convert_to_integer(roman_number):
    roman_values = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    total = 0

    for index in range(len(roman_number) - 1):
        if roman_values[roman_number[index]] < roman_values[roman_number[index + 1]]:
            total -= roman_values[roman_number[index]]
        else:
            total += roman_values[roman_number[index]]

    return total + roman_values[roman_number[-1]]


user_input = input("Enter a Roman numeral: ").upper()

print("Integer equivalent:", convert_to_integer(user_input))
