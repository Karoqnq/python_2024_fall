def print_pyramid(height):

    for i in range (1, height + 1): # 1 to height hence + 1
        print(i * "*")

def main():

    height = int(input("Enter pyramid height: "))
    print_pyramid(height)

main()