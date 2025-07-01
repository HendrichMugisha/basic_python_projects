#this is a version of the pig-dice game attempted using classes
import random


class Game:
    def __init__(self,points, player_Id):
        self.points=points
        self.player_Id=player_Id

    def switch_player(self, player_Id):
        if player_Id == 1:
            player_2.play_game()
        elif player_Id == 2:
            player_1.play_game()

    def roll_again(self):
        choice = input("Roll again? (y/n): ").lower()
        if choice =='y':
            self.play_game()
        elif choice == 'n':
            print(f"You scored {self.points} points in this turn.")
            self.switch_player(self.player_Id)

    def play_game(self):
        while True:
            print(f"\nPlayer{self.player_Id}'s turn")
            temp=random.randint(1,6)
            print(f"You rolled a {temp}")
            if temp == 1:
                self.points=0
                print("You scored 0 points in this round!")
                self.switch_player(self.player_Id)
            else:
                self.points+=temp
                print(f"Current score: {self.points}")
            if self.points<50:
                self.roll_again()
            else:
                print(f"Player{self.player_Id} is the winner with {self.points} points!")
                break



player_1 = Game(0, 1)
player_2 = Game(0, 2)    

player_1.play_game()