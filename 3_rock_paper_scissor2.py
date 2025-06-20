#the mighty rock, paper and scissors game
import random

def win(computer_choice, user_choice):
    print(f"Computer Chose {computer_choice}\nYou Chose {user_choice}\nYou Win!")
def lose(computer_choice, user_choice):
    print(f"Computer Chose {computer_choice}\nYou Chose {user_choice}\nYou Lose!")

def cont():
    check=input("would you like to continue?: (y/n) ").lower()
    if check=='y':
        return True
    elif check=='n':
        return False
    else:
        replay()
    
def replay():
    if cont():
        play()
    else:
        return False
#generate a random number

def play():
    while True:
        r, p, s = 'rock'[0], 'paper'[0], 'scissors'[0]
        computer_choice=random.choice([r,p,s])
        print(computer_choice)

        #ask user to enter input and validate it
        user_choice=input("Rock, Paper or Scissors? (r/p/s): ")
        test=1
        if user_choice==r or user_choice==p or user_choice==s:
            test=1
        else:
            test=2

        # user result from validation to proceed with program accordingly
        if test==2:
            print("Please enter r/p/s: ")
        else:
            # the tie condition
            if computer_choice == user_choice:
                if computer_choice=='r':
                    print("you both chose Rock!")
                    if replay() ==False:
                        break
                elif computer_choice == 'p':
                    print('you both chose Paper! ')
                    if replay() ==False:
                        break
                else:
                    print('you both choce Scissors! ')
                    if replay() ==False:
                        break
            
            #the win/loss conditions
            if computer_choice=='r':
                if user_choice=='p':
                    win(computer_choice, user_choice)
                    if replay() ==False:
                        break
                elif user_choice=='s':
                    lose(computer_choice, user_choice)
                    if replay() ==False:
                        break
            
            elif computer_choice=='p':
                if user_choice=='r':
                    lose(computer_choice, user_choice)
                    if replay() ==False:
                        break
                elif user_choice=='s':
                    win(computer_choice, user_choice)
                    if replay() ==False:
                        break
            
            elif computer_choice=='s':
                if user_choice=='r':
                    win(computer_choice, user_choice)
                    if replay() ==False:
                        break
                elif user_choice=='p':
                    lose(computer_choice, user_choice)
                    if replay() ==False:
                        break

play()         






















#loop
#ask user to make a choice
#if choice is invalid, ask them to remake the choice
#else print their choice
#print computer choice
# print result
#ask to continue
