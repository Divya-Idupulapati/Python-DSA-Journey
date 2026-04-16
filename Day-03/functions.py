# Function = A block of reusable code
# place () after the function name to invoke it
# def happy_brithday(name, age=30):
#     print(f"Happy Birthday to {name}!")
#     print("May god bless you dear!")
#     print(f"You are {age} years old!")
#     print("Happy Birthday to you!")
#     print()


# happy_brithday("Bro", 20)
# happy_brithday("Steve")
# happy_brithday("Joe", 40)


# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due:{due_date}")


# display_invoice("BroCode", 100.01, "01/02")


# Return =  Statement used to end a function
#           and send a result back to the caller


# def add(x, y):
#     z = x + y
#     return z


# def subtract(x, y):
#     z = x - y
#     return z


# def multiply(x, y):
#     z = x * y
#     return z


# def divide(x, y):
#     z = x / y
#     return z


# print(add(2, 3))
# print(subtract(2, 3))
# print(multiply(2, 3))
# print(divide(2, 3))


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last


full_name = create_name("spongebob", "squarepants")
print(full_name)
