selling_price = int(input("Enter the car's selling price: "))

if 20000 < selling_price < 50000:
    bonus = selling_price * 0.01
    print(f"The bonus is {bonus:.2f} euros.")

elif selling_price >= 50000:
    bonus = selling_price * 0.015
    print(f"The bonus is {bonus:.2f} euros.")

else:
    print("The bonus is 200.00 euros.")