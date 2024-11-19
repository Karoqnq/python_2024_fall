gigs = int(input("Number of gigs: "))
same_strings = int(input("Gigs to be played with the same set of strings: "))
price_per_set = float(input("Price of a set of guitar strings: "))


new_sets = (gigs - 1) // same_strings + 1
total_cost = new_sets * price_per_set


print(f"The guitarist needs {new_sets} new sets of guitar strings")
print(f"The total cost is {total_cost:.2f} euros")

#did get help for the calc part because I was stuck on it and didn't realize how the rounding worked