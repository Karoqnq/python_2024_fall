#Just a test exercise for myself
def push_forward(how_much_time, add_years, add_months, add_days):
    #tuple time days, months, years
    #nr of months and nr of days to be added

    years, months, days = how_much_time

    total_days = days + add_days
    additional_months = total_days // 30
    new_days = total_days % 30

    total_months = months +  add_months + additional_months
    additional_years = total_months // 12
    new_months = total_months % 12

    total_years = years + add_years + additional_years

    return total_years, new_months, new_days

def main():

    print("Current time of procrastination 00:00:00")
    how_much_time_left = (0,0,0)

    while True:
        add_years = int(input("Enter years to add: "))
        if add_years < 0:
            break

        add_months = int(input("Enter months to add: "))
        if add_months < 0:
            break

        add_days = int(input("Enter days to add: "))
        if add_days < 0:
            break

        how_much_time_left = push_forward(how_much_time_left, add_years, add_months, add_days)

        print(f"Time procrastinated {how_much_time_left[0]} years, {how_much_time_left[1]} months, and {how_much_time_left[2]} days")
    
if __name__ == "__main__":
    main()

