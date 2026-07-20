from math import sqrt

user_number = int(input("Enter a number: "))

print()

if user_number > 1:
    for divisor in range(2, int(sqrt(user_number)) + 1):
        if user_number % divisor == 0:
            print(user_number, "is not a prime number")
            break
    else:
        print(user_number, "is a prime number")
else:
    print(user_number, "is not a prime number")
