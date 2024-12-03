def common_members(list_one: list, list_two: list):

    for i in list_one: # Go through all members in list one
        if i in list_two: # If you hit a member in list two who matches with list one return true
            return True
        
    return False

def main():

    list_one = []
    list_two = []

    for i in range (5):
        member_one = input("Enter a member to list one: ")
        list_one.append(member_one)
    
    for i in range (5):
        member_two = input("Enter a member to list two: ")
        list_two.append(member_two)

    result = common_members(list_one, list_two)

if __name__ == "__main__":
 main()