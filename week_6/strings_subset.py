first_str = input("Enter first string: ")
second_str = input("Enter second string: ")
subset_true = True # Boolean variable

if not second_str: # If there is no input for second string there's nothing to be checked
    print("Nothing to be checked")
    
else:
    for letter in second_str: # Loop through all letters of the second string
        if letter not in first_str: # If letter not in the first string then subset is false
            subset_true = False
            break

if subset_true:
    print("Subset")
else:
    print("Not subset")