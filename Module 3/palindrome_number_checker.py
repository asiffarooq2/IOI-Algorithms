user_number = int(input("Enter a number: "))

input_number = user_number
reverse_value = 0

while user_number > 0:
    current_digit = user_number % 10
    reverse_value = reverse_value * 10 + current_digit
    user_number //= 10

if input_number == reverse_value:
    print(input_number, "is a palindrome")
else:
    print(input_number, "is not a palindrome")
