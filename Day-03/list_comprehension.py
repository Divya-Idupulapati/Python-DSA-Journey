# list_comprehension - A concise way to create lists in python
#                     Compact and easier to read than traditional loops
#                     [expression for value in iterable if condition]

doubles = [x * 2 for x in range(1, 11)]
triples = [x * 3 for x in range(1, 11)]
squares = [x * x for x in range(1, 11)]
print(doubles)
print(triples)
print(squares)

fruits = [fruit.upper() for fruit in ["apple", "orange", "banana", "coconut"]]
print(fruits)

fruit_char = [fruit[0] for fruit in fruits]
print(fruit_char)
