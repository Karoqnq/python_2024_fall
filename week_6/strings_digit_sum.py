user_string = input("Enter a string: ")
string_sum = 0

for d in user_string:

    if d.isdigit():
        string_sum += int(d)
    
print(f"The sum of digits is {string_sum}")