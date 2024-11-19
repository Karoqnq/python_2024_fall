def print_rectangle():
    
    height = int(input("Enter height: "))
    width = int(input("Enter width: "))

    for row in range (height):
        for column in range (width):
            print("*", end="")
        print()

def main():
    print_rectangle()
main()