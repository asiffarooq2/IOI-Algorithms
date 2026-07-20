def find_factors(value):
    print("The factors of", value, "are:")

    for divisor in range(1, value + 1):
        if value % divisor == 0:
            print(divisor)


user_number = int(input("Enter a number: "))

find_factors(user_number)
