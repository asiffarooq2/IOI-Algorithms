first_number = 56
second_number = 12

print("================================")
print("BITWISE SWAP CHALLENGE")
print("================================")

print("\nPART 1: Swap Without a Third Variable")
print("Before Swap:")
print("First Number =", first_number)
print("Second Number =", second_number)

first_number = first_number + second_number
second_number = first_number - second_number
first_number = first_number - second_number

print("After Swap:")
print("First Number =", first_number)
print("Second Number =", second_number)

xor_first = 45
xor_second = 18

print("\nPART 2: XOR Swap")
print("Before XOR Swap:")
print("First Value =", xor_first)
print("Second Value =", xor_second)

xor_first ^= xor_second
xor_second ^= xor_first
xor_first ^= xor_second

print("After XOR Swap:")
print("First Value =", xor_first)
print("Second Value =", xor_second)

shift_number = 3

print("\nPART 3: Left Shift Doubles the Number")
print("Original Number:", shift_number)

print(shift_number, "<< 1 =", shift_number << 1)
print(shift_number, "<< 2 =", shift_number << 2)
print(shift_number, "<< 3 =", shift_number << 3)
print(shift_number, "<< 4 =", shift_number << 4)

print("Each left shift multiplies the number by 2.")

first_value = -10
second_value = 5

print("\nPART 4: XOR for Sign Detection")
print("First Value =", first_value)
print("Second Value =", second_value)

if (first_value < 0) ^ (second_value < 0):
    print("The numbers have different signs.")
else:
    print("The numbers have the same sign.")

dividend = 25
divisor = 4

quotient = 0
remaining_value = dividend

while remaining_value >= divisor:
    remaining_value -= divisor
    quotient += 1

print("\nPART 5: Divide Without '/'")
print("Dividend:", dividend)
print("Divisor:", divisor)
print("Quotient:", quotient)
print("Remainder:", remaining_value)

print("\n================================")
print("BITWISE SWAP CHALLENGE SUMMARY")
print("================================")
print("Swap without a third variable uses addition and subtraction.")
print("XOR swap uses the ^ operator to exchange values.")
print("Left shift doubles a number.")
print("XOR can detect whether two numbers have different signs.")
print("Division can be performed using repeated subtraction.")
print("================================")
