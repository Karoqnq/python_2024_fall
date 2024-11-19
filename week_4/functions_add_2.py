def add(a, b):

   return int(a + b + 0.5) # Pushes it into the next integer. When converting it is going to round down and this helps to round it to the correct number.

def main():

    x = float(input("Enter a float: "))
    y = float(input("Enter a float: "))

    result = add(x, y)

    print(result)

    if __name__ == "__main__":
        main()