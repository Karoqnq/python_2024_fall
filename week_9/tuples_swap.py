def tuples_swap()
# input 7 integers from the user and save them in a list
num_list = []

for i in range(7):
    num = int(input("Enter an integer: "))
    num_list.append(num)

# Then swap each successive pair of elements in the list and print it.

print(num_list[::2])

def main()
    
    tuples_swap()