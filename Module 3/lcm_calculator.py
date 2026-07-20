first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

largest = max(first_number, second_number)

while True:
    if largest % first_number == 0 and largest % second_number == 0:
        print("LCM is:", largest)
        break
    largest += 1
