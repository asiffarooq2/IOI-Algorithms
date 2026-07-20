def find_prime_numbers(limit):
    is_prime = [True] * (limit + 1)

    current = 2

    while current * current <= limit:
        if is_prime[current]:
            for multiple in range(current * current, limit + 1, current):
                is_prime[multiple] = False
        current += 1

    for number in range(2, limit + 1):
        if is_prime[number]:
            print(number)


user_limit = int(input("Enter a number: "))

print("Prime numbers less than or equal to", user_limit, "are:")

find_prime_numbers(user_limit)
