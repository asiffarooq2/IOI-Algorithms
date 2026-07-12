# ================================
# SET UNION
# FRUITS COLLECTION
# ================================

# Create two sets
basket1 = {"Apple", "Banana", "Orange", "Mango"}
basket2 = {"Mango", "Grapes", "Apple", "Pineapple"}

print("Basket 1:", basket1)
print("Basket 2:", basket2)

# Union using union() method
all_fruits = basket1.union(basket2)

print("\nUnion of Basket 1 and Basket 2:")
print(all_fruits)

# Union using | operator
all_fruits2 = basket1 | basket2

print("\nUnion using | operator:")
print(all_fruits2)

print("\nTotal Unique Fruits:", len(all_fruits))
