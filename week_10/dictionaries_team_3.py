team_members = {"John": "software developer", "Ann": "project manager", "Susan": "software developer", "Jill": "lead developer"}

while True:
    who_are_you = input("Enter name (quit ends): ")

    if who_are_you.lower() == "quit":
        break

    if who_are_you not in team_members:
        print(f"{who_are_you} is not in the team")
        print()

    else:
        print(f"{who_are_you} is a {team_members[who_are_you]}")
        print()
    