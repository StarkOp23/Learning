# Mutable

spice_mix = set()  # Data type, represents collection of things
print(f"Initial ID of Spice Mix: {id(spice_mix)}")
spice_mix.add("pepper")
spice_mix.add("Salt")
print(f"After ID of Spice Mix: {id(spice_mix)}")


# Immutable

spice_mix = ("pepper", "Salt")
print(f"Initial ID of Spice Mix: {id(spice_mix)}")
spice_mix = ("pepper", "Salt", "Cayenne")
print(f"After ID of Spice Mix: {id(spice_mix)}")
