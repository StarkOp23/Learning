# String ======================

customer_name = "Soumyadeep"
Meal = "Protein Shake"
print(f"{customer_name} ordered : {Meal}")
Meal_description = "Protien shake with 2 scoops of protein powder"
print(f"First word : {Meal_description[:8]}")
print(f"Last word : {Meal_description[9:]}")
print(f"Reverse order : {Meal_description[::-1]}")
# print(f"First word : {Meal_description.split()[0]}")



labeled_text = "Spam and éggs"

encoded = labeled_text.encode("utf-8")
print(f"Encoded: {encoded}")

decoded = encoded.decode("utf-8")
print(f"Decoded: {decoded}")
