import random

#dictionary that stores player indeces and the list of their result rolls
players_dict = {
    1:[],
    2:[]
}

# players_dict[1].append(2)
# print(players_dict[1])
#list of all the player ID's
players_list=list(players_dict.keys())

def switch_player(player_index):
    if player_index==1:
        player_index=2
    else:
        player_index=1
    return player_index


def play_game():
    player_index=players_list[0]

    while True:
        print(f"\nPlayer{player_index}'s turn: ")
        result=random.randint(1,6)
        print(f'You rolled a {result}')

        if result==1:
            players_dict[player_index]=[]
            # choice=input("Roll again? (y/n): ").lower()
            player_index=switch_player(player_index)

        else:
            players_dict[player_index].append(result)
            print(f"Current scores: Player {players_list[0]}: {sum(players_dict[players_list[0]])}, Player {players_list[1]}: {sum(players_dict[players_list[1]])}\n")

            choice=input("Roll again? (y/n): ").lower()
            if choice=='y':
                pass
            elif choice=='n':
                player_index=switch_player(player_index)
                continue
            else:
                pass

play_game()