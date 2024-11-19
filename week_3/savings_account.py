interest_rate = float(input("Enter interest rate: ")) / 100 # Converting it into a decimal
tax_rate = float(input("Enter capital income tax rate: ")) / 100 # Converting it into a decimal
initial_deposit = float(input("Enter initial deposit: "))
years = int(input("Enter number of years: "))
print()

balance = initial_deposit

for year in range (1, years + 1, 1):

    interest = balance * interest_rate # Interest for the current year

    taxed_interest = interest * (1 - tax_rate) # Subtract the tax from the interest

    balance = balance + taxed_interest # Add to the balance

    print(f"Year {year}: {balance:.2f}")
