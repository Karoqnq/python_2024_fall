def roll_forward(clock_time, add_hours, add_minutes):
    #clock time as a tuple which contains hours int and minutes int
    # Num of hours to be added to the clock time
    # Num of minutes to be added to the clock time
    # return new time

    hours, minutes = clock_time

    total_minutes = minutes + add_minutes
    additional_hours = total_minutes // 60 # round down to nearest integer
    new_minutes = total_minutes % 60 # remainder of minutes

    total_hours = hours + add_hours + additional_hours
    new_hours = total_hours % 24 # Make sure that it doesn't go over 23 with hours

    return new_hours, new_minutes

def main():

    print("The current time is 00:00")
    current_time = (0,0)

    while True:
        add_hours = int(input("Enter hours to add: "))
        if add_hours < 0:
            break
        
        add_minutes = int(input("Enter minutes to add: "))
        if add_minutes < 0:
            break

        current_time = roll_forward(current_time, add_hours, add_minutes)
        print(f"{current_time[0]:02}:{current_time[1]:02}") # use :02 for the 00 structure

if __name__ == "__main__":
    main()