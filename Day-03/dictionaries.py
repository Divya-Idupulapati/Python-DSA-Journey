# Dictionary = A collection of the {key:value} pairs
# Ordered and changeable. No duplicates.

capitals = {
    "USA": "Washington DC",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow",
}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("India"))
"""
if capitals.get("Russia"):
    print("That capital Exists")
else:
    print("That capital doesn't exsit")
"""

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detoroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()
# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# for value in capitals.values():
#     print(value)

# items = capitals.items()
# print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")
