"""
Problem:-
Write a Python program that checks whether a password is strong or weak.

A password is strong if:
1. length is at least 16
2. contains at least one uppercase letter
3. contains at least one lowercase letter
4. contains at least one digit
5. contains at least 1 special character
6. does not contain spaces
7.does not contain 3 repeated consecutive characters like aaa or 111

If all conditions are true, print "Strong Password", otherwise print "Weak Password".

Example
Input: Pyth0n@@Master99
Output:
Password Report
----------------------------------------
Original Length      : 16
Uppercase Count      : 2
Lowercase Count      : 10
Digit Count          : 3
Special Count        : 2
Masked Password      : Py************99
Strength             : STRONG


Add a retry system using while loop:
user gets only 3 attempts. If password is weak, ask again.
Stop when strong password is entered or attempts finish
"""

print(
    """Pasword rules:
1. length is at least 12
2. contains at least one uppercase letter
3. contains at least one lowercase letter
4. contains at least one digit
5. contains at least 1 special character
6. does not contain spaces
7. does not contain 3 repeated consecutive characters like aaa or 111"""
)
attempt = 1
while attempt <= 3:
    password = input("Enter the password:")

    length_pass = len(password)
    Is_upper = False
    Is_lower = False
    Is_digit = False
    Is_space = False
    Is_special = False
    Is_cons = False
    upper_count = 0
    lower_count = 0
    digit_count = 0
    special_count = 0
    for ch in password:
        if ch.isupper():
            upper_count += 1
            Is_upper = True
        elif ch.islower():
            lower_count += 1
            Is_lower = True
        elif ch.isdigit():
            digit_count += 1
            Is_digit = True
        elif ch == " ":
            Is_space = True
        else:
            special_count += 1
            Is_special = True

    for i in range(length_pass - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            Is_cons = True
            break

    if (
        (length_pass >= 12)
        and (Is_upper == True)
        and (Is_lower == True)
        and (Is_digit == True)
        and (Is_special == True)
        and (Is_space == False)
        and (Is_cons == False)
    ):
        strength = "STRONG"
        print(f"Orginal Length: {length_pass}")
        print(f"Uppercase Count: {upper_count}")
        print(f"Lowercase Count: {lower_count}")
        print(f"Digit Count: {digit_count}")
        print(f"Special Count: {special_count}")
        print(
            f"Masked Password: {password[0:2]+ "*" * (length_pass - 4) + password[-2:]}"
        )
        print(f"Strength:{strength}")
        break
    else:
        print("Password is weak")
        if attempt < 3:
            print(f"Try again, {3 - attempt} attempts left")
        else:
            print("All attempts failed!! Try after sometime.")
        attempt += 1
