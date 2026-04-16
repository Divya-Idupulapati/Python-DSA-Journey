# Membership operators - used to test whether a value or variable is found in a sequence
# (string, list, tuple , set or dictionary)
# 1. in
# 2. not in

word = "Apple"
letter = input("Guess a letter in the secret word:")
# if letter in word:
#     print(f"{letter} was found")
# else:
#     print(f"{letter} was not found")


if letter not in word:
    print(f"{letter} was not found")
else:
    print(f"{letter} was found")
