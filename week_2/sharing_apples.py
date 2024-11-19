apples = int(input("How many apples? "))
children = int(input("How many children? "))


each_child = apples // children
left_over = apples % children

print()
print(f"Each child will get {each_child} apples.")
print(f"There will be {left_over} leftover apples.")