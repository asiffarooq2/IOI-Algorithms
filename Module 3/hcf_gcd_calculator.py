first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

while second_number != 0:
    remainder = second_number
    second_number = first_number % second_number
    first_number = remainder

print("HCF is:", first_number)
