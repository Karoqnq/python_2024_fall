def compute_earnings(wage, hours):

    if hours > 40:
        earnings = (40 * wage) + (hours - 40) * (1.5 * wage)
    else:
        earnings = wage * hours

    return earnings


def main():
    wage = float(input("Enter wage: "))
    hours = int(input("Enter hours: "))

    earnings = compute_earnings(wage, hours)

    print(f"The earnings are {earnings:.2f}")
    
main()