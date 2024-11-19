def double_factorial(n):

    if n < 0:
        return("Please enter a non-negative integer")
    
    result = 1
    
    if n == 0: # If the input is 0, return 1 since 0!! is 1
        return result
    
    # Determine whether even or odd.
    if n % 2 == 0: 
        for i in range(2, n + 1, 2): # if even, multiply the even numbers from 2 to n
            result = result * i
       
    else:
        for i in range(1, n + 1, 2): # if odd, multiply the odd numbers from 1 to n
            result = result * i

    return result

def main():

    for i in range(10):
        print(f"{i}!! = {double_factorial(i)}")

main()