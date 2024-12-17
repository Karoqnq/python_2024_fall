def print_player(player_tuple):

    team_name, player_name, nr_of_goal = player_tuple

    print(f"{player_name} ({team_name}), {nr_of_goal} goals")

def main():
    p = ("Hawks", "Jennifer", 10)
    print_player(p)

main()

