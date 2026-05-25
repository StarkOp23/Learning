# Tuples ===========================
# What is Tuple do ?
# A tuple in Python is a built-in data type used to store multiple items in a single variable.

# Tuples are:

# Ordered → items keep their position
# Immutable → cannot be changed after creation
# Allow duplicates
# Faster than lists in some cases

Dishes = ("Biriyani", "Pizza", "Burger")
Dish1, Dish2, Dish3 = Dishes
# Un-packing
print(f"First Dish: {Dish1}")
print(f"Second Dish: {Dish2}")
print(f"Third Dish: {Dish3}")

A, B = 2, 3
print(f"Value of A: {A} and B: {B}")
# Swap
A, B = B, A
print(f"Value of A: {A} and B: {B}")


# membership (Case Sensitive)
print(f"Is Biriyani in Dishes? {'Biriyani' in Dishes}")

print(f"Is Pulao in Dishes? {'Pulao' in Dishes}")
