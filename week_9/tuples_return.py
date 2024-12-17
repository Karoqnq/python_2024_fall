def pow_2_3(num):
    #compute 2nd and 3rd power of the integer and return it as a tuple
    pow_2 = num ** 2
    pow_3 = num ** 3

    return (pow_2, pow_3)


def main():
    x = int(input("Enter an integer: "))
    p2, p3 = pow_2_3(x)

    print(p2)
    print(p3)

if __name__ == "__main__":
    main()