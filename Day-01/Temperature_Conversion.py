# Temperature conversion program
unit = input("Is this temperature in celsius or Fahrenheit (C/F):")
temp = float(input("Enter the temperature:"))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(
        f"The temperature in Fahrenheit is: {temp}°F"
    )  # shift + option + 8 = ° in mac ; alt + 0176 in windows
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celcius is: {temp}°C")
else:
    print(f"{unit} is and invalid unit of measurement.")
