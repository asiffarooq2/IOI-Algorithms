device_status = 45


def binary_format(value):
    return bin(value)[2:]


print("================================")
print("MY SMART SWITCH BIT MONITOR")
print("================================")

print("Switch Value:", device_status)
print("Binary Form:", binary_format(device_status))

binary_string = binary_format(device_status)

active_switches = binary_string.count("1")
inactive_switches = binary_string.count("0")

print("\nPART 1: Set Bits and Zero Bits")
print("Set Bits / ON Switches:", active_switches)
print("Zero Bits / OFF Switches:", inactive_switches)

set_bit_total = 0
current_value = device_status

while current_value > 0:
    if current_value & 1:
        set_bit_total += 1
    current_value >>= 1

print("\nPART 2: Counting Set Bits")
print("Number of ON Switches:", set_bit_total)

first_active_position = 1
current_value = device_status

while current_value > 0:
    if current_value & 1:
        break
    first_active_position += 1
    current_value >>= 1

print("\nPART 3: The First Set Bit")
print("First ON Switch Position:", first_active_position)

print("\nPART 4: Building a Bit Mask")

for bit_position in range(6):
    bit_mask = 1 << bit_position
    print("Bit", bit_position, "Mask:", bit_mask,
          "Binary:", binary_format(bit_mask))

device_names = [
    "Living Room Light",
    "Fan",
    "Air Conditioner",
    "Door Lock",
    "Garden Light",
    "Security Camera"
]

print("\nPART 5: Check if the Nth Bit is Set")

for bit_position in range(6):
    bit_mask = 1 << bit_position

    if device_status & bit_mask:
        print("Bit", bit_position, "-", device_names[bit_position], "is ON")
    else:
        print("Bit", bit_position, "-", device_names[bit_position], "is OFF")

print("\n================================")
print("SMART SWITCH SUMMARY")
print("================================")
print("Switch Value:", device_status)
print("Binary Form:", binary_format(device_status))
print("Total ON Switches:", set_bit_total)
print("First ON Switch Position:", first_active_position)
print("================================")
