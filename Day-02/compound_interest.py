"""
A = P(1+ R/N)^NT

A - FINAL AMOUNT
P - PRINCIPAL AMOUNT
R - ANNUAL INTEREST RATE
N - NUMBER OF COMPOUNDING PERIODS (e.g., 12 for monthly, 4 for quarterly)
T - TIME( EXPRESSED IN YEARS)
"""

N = 1

while True:
    principal_amt = float(input("Enter the principal amount"))
    if principal_amt < 0:
        print("Principal amt can't be zero.")
    else:
        break

while True:
    Rate = float(input("Enter the interest rate"))
    if Rate < 0:
        print("Interest can't be zero.")
    else:
        Rate = Rate / 100  # eg:- 10% = 10 / 100
        break

while True:
    Time = float(input("Enter the time in years:"))
    if Time < 0:
        print("Time can't be zero.")
    else:
        break

Final_amt = principal_amt * pow((1 + Rate / N), (N * Time))
print(f"Total final amount owed is:{Final_amt}")
