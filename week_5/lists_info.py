integers = []
count = 0

for i in range (5): 
    new_int = int(input("Enter an integer: "))
    integers.append(new_int) 
    count += 1

print()
print(f"Count: {count}")
print(f"min: {min(integers)}")
print(f"max: {max(integers)}")
print(f"sum: {sum(integers)}")