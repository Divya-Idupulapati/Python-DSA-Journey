# python calculator

operator = input("Enter an operator (+, -, *, /)")
a = int(input("Enter a number a:"))
b = int(input("Enter a number b:"))
if operator == "+":
    print(f"Sum of two numbers is:{a+b}")
elif operator == "-":
    print(f"Difference of two numbers is:{a-b}")
elif operator == "*":
    print(f"Product of two numbers is:{a*b}")
elif operator == "/":
    print(f"Quotient of two numbers after dividing a & b:{a/b}")
else:
    print("Enter a valid operator")
