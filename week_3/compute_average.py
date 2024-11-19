x = float(input("Enter first number: "))

if x == 0:  
    print("Nothing to be calculated")

else:
    sum = 0
    count = 0

    while x != 0:
        sum += x
        count += 1
        x = float(input("Enter next number: "))

    average = sum / count
    print(f"The average is {average:.2f}")
