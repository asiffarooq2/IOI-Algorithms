number = int(input("Enter a number: "))

digit_count = len(str(number))

sum_of_powers = 0
temp_number = number

while temp_number > 0:
    current_digit = temp_number % 10
    sum_of_powers += current_digit ** digit_count
    temp_number //= 10

if number == sum_of_powers:
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
