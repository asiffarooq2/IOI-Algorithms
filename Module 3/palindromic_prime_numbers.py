limit = 3000

for current_number in range(1, limit + 1):
    factor_count = 0
    reversed_number = 0
    temp_number = current_number

    for divisor in range(1, temp_number + 1):
        if temp_number % divisor == 0:
            factor_count += 1

    if factor_count == 2:
        while temp_number > 0:
            reversed_number = reversed_number * 10 + (temp_number % 10)
            temp_number //= 10

        if reversed_number == current_number:
            print(current_number)
