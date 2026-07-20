primary_code = 13
secondary_code = 9


def binary_format(value, width=4):
    return format(value & ((1 << width) - 1), f"0{width}b")


print("================================")
print("MY SECRET CODE BIT SCANNER")
print("================================")
print("Primary Code:", primary_code, "Binary:", binary_format(primary_code))
print("Secondary Code:", secondary_code,
      "Binary:", binary_format(secondary_code))

print("\nPART 1: Bits and Binary")
print("Binary numbers use only 0 and 1.")
print("Primary Code Binary:", binary_format(primary_code))
print("Secondary Code Binary:", binary_format(secondary_code))

and_value = primary_code & secondary_code
or_value = primary_code | secondary_code

print("\nPART 2: AND and OR")
print("AND Result:", and_value, "Binary:", binary_format(and_value))
print("OR Result:", or_value, "Binary:", binary_format(or_value))
print("AND keeps only positions where both bits are 1.")
print("OR keeps positions where at least one bit is 1.")

not_value = (~primary_code) & 0b1111
xor_value = primary_code ^ secondary_code

print("\nPART 3: NOT and XOR")
print("NOT Primary Code within 4 bits:", not_value,
      "Binary:", binary_format(not_value))
print("XOR Result:", xor_value, "Binary:", binary_format(xor_value))
print("XOR gives 1 when the compared bits are different.")

left_shift_value = primary_code << 1
right_shift_value = primary_code >> 1

print("\nPART 4: Left Shift and Right Shift")
print("Left Shift Result:", left_shift_value,
      "Binary:", binary_format(left_shift_value, 5))
print("Right Shift Result:", right_shift_value,
      "Binary:", binary_format(right_shift_value))
print("Left shift moves bits left. Right shift moves bits right.")

xor_check = primary_code ^ 1

print("\nPART 5: Odd or Even with XOR")
print("Primary Code XOR 1:", xor_check)

if xor_check == primary_code - 1:
    print("Primary Code is Odd because XOR with 1 reduced it by 1.")
else:
    print("Primary Code is Even because XOR with 1 increased it by 1.")

set_bit_count = primary_code.bit_count()

print("\nPART 6: Counting Bits")
print("Number of 1 bits in Primary Code:", set_bit_count)

print("\n================================")
print("SECRET CODE SCAN SUMMARY")
print("================================")
print("Primary Code:", primary_code, "Binary:", binary_format(primary_code))
print("Secondary Code:", secondary_code,
      "Binary:", binary_format(secondary_code))
print("AND:", and_value)
print("OR:", or_value)
print("NOT within 4 bits:", not_value)
print("XOR:", xor_value)
print("Left Shift:", left_shift_value)
print("Right Shift:", right_shift_value)
print("1 Bits Count:", set_bit_count)
print("================================")
