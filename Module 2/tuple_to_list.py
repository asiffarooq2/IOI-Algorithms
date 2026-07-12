# ================================
# TUPLE TO LIST
# MOBILE PHONES
# ================================

# Create a tuple
phones = ("Samsung", "Apple", "OnePlus", "Xiaomi", "Realme")

print("Original Tuple:")
print(phones)

# Convert tuple into a list
phone_list = list(phones)

print("\nConverted List:")
print(phone_list)

# Modify the list
phone_list.append("Google Pixel")
phone_list.remove("Xiaomi")

print("\nUpdated List:")
print(phone_list)

# Display the type of both variables
print("\nType of phones:", type(phones))
print("Type of phone_list:", type(phone_list))
