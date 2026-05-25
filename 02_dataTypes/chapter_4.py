#! Boolean =================================================================

is_boling = True
stir_count = 5

total_actions = is_boling + stir_count  # Upcasting True to 1
print(total_actions)

is_milk_hot = 0
print(f"Is Milk Hot: {bool(is_milk_hot)}")


hot_water = True
tea_added = True
can_serve = hot_water and tea_added
print(f"Can Serve: {can_serve}")