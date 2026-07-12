# ================================
# LISTS TO DICTIONARY
# FRUIT PRICE DIRECTORY
# ================================

# Create two lists
fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes"]
prices = [120, 40, 80, 150, 90]

print("Fruits:", fruits)
print("Prices:", prices)

# Convert lists into a dictionary
fruit_price = dict(zip(fruits, prices))

print("\nFruit Price Dictionary:")
print(fruit_price)

# Access values
print("\nPrice of Mango:", fruit_price["Mango"])
print("Price of Apple:", fruit_price["Apple"])

# Display all keys
print("\nAvailable Fruits:", fruit_price.keys())

# Display all values
print("Prices:", fruit_price.values())

# Display all key-value pairs
print("Fruit and Price List:", fruit_price.items())
