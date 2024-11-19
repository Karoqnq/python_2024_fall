number_of_visits = int(input("Enter the number of days of gym visits per year: "))
day_pass_price = float(input("Enter price for a day pass: "))
membership_fee = float(input("Enter yearly membership fee: "))

total_day_pass_cost = number_of_visits * day_pass_price

if total_day_pass_cost < membership_fee:
    print()
    print(f"Buying day passes is {membership_fee - total_day_pass_cost:.2f} euros cheaper")
	
elif membership_fee < total_day_pass_cost:
    print()
    print(f"Paying the yearly membership fee is {total_day_pass_cost - membership_fee:.2f} euros cheaper")
	
else:
    print()
    print("There is no price difference")