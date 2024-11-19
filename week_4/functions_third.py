def compute_discount(price, discount_percentage):

    discount = price * discount_percentage
    return discount

def main():
    price = float(input("Enter price: "))
    discount_percentage = float(input("Enter discount percentage: ")) / 100 # Make into decimal

    print(f"The discount is {compute_discount(price, discount_percentage):.2f} euros")

main()
