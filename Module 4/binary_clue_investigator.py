first_number = 7
second_number = 7

print("================================")
print("BINARY CLUE INVESTIGATOR")
print("================================")

print("\nPART 1: XOR Identity and Equality")
print("First Number =", first_number)
print("Second Number =", second_number)
print("a ^ a =", first_number ^ first_number)
print("a ^ 0 =", first_number ^ 0)

if (first_number ^ second_number) == 0:
    print("Both numbers are equal")
else:
    print("Both numbers are different")

clue_numbers = [3, 5, 3, 5, 9]

xor_value = 0

for clue in clue_numbers:
    xor_value ^= clue

print("\nPART 2: XOR Cancellation")
print("Clues:", clue_numbers)
print("Final XOR Result:", xor_value)
print("Repeated clues cancel out, so the remaining clue is:", xor_value)

number_list = [4, 7, 4, 2, 7, 2, 9]

single_odd = 0

for value in number_list:
    single_odd ^= value

print("\nPART 3: One Odd-Occurring Number")
print("Numbers:", number_list)
print("Odd-occurring Number:", single_odd)

pair_list = [3, 9, 3, 5, 5, 7]

combined_xor = 0

for value in pair_list:
    combined_xor ^= value

print("\nPART 4: XOR of Two Odd-Occurring Numbers")
print("Numbers:", pair_list)
print("XOR of Two Odd-Occurring Numbers:", combined_xor)

rightmost_set_bit = combined_xor & -combined_xor

first_odd_number = 0
second_odd_number = 0

for value in pair_list:
    if value & rightmost_set_bit:
        first_odd_number ^= value
    else:
        second_odd_number ^= value

print("\nPART 5: Splitting by the Rightmost Set Bit")
print("Rightmost Set Bit:", rightmost_set_bit)
print("First Odd-Occurring Number:", first_odd_number)
print("Second Odd-Occurring Number:", second_odd_number)

print("\n================================")
print("BINARY CLUE INVESTIGATION SUMMARY")
print("================================")
print("XOR Identity: a ^ a = 0")
print("XOR with Zero: a ^ 0 = a")
print("XOR Cancellation removes repeated pairs")
print("One Odd-Occurring Number:", single_odd)
print("Two Odd-Occurring Numbers:", first_odd_number, "and", second_odd_number)
print("================================")
