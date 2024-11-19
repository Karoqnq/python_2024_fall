decimal_number = float(input("Enter a decimal number: "))
two_decimals = round(decimal_number, 2)
four_decimals = round(decimal_number, 4)

print(two_decimals)
print(four_decimals)

decimal_number = float(input("Enter a decimal number: "))

print(f"{decimal_number:.2f}")
print(f"{decimal_number:.4f}")