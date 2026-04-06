"""Write a program that takes salary as input and calculates the final tax based on these rules:

If salary < 30,000 → 5% tax
If salary is between 30,000 and 70,000 → 15% tax
If salary > 70,000 → 25% tax"""

input = float(input("Enter the salary:"))

if input < 30000:
    tax = input * 0.05
    print(f"Final tax is:{tax}")
elif input >= 30000 and input <= 70000:
    tax = input * 0.15
    print(f"Final tax is:{tax}")
else:
    tax = input * 0.25
    print(f"Final tax is:{tax}")
