import random

def replay():
    check=input("would you like to play again? (y/n): ").lower()
    if check=='y' or check == 'n':
        if check=='y':
            return True
        elif check=='n':
            return False
        else:
            replay()
        
def play():
    number_to_guess=random.randint(1,100)

    while True:
        try:
            guess=int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print('please enter a valid discount')


        if guess>number_to_guess:
            print("Too high!")
        elif guess<number_to_guess:
            print("Too low!")
        else:
            print("you guessed the number!")
            if replay():
                play()
            else:
                break

play()
        























# import random

# def check(guess):
#     try:
#         int(guess)

#         return True
#     except ValueError:
#         return False

# answer=random.randint(1,100)

# while True:
#     guess=int(input("Enter a number between 1 and 100: "))
#     if check(guess):
#         if guess>=1 and guess<=100:
#             if guess==answer:
#                 print("You guessed the number!")
#                 break
#             elif guess<answer:
#                 print("Too low!")
#             elif guess>answer:
#                 print("Too high!")
#         else:
#             print("Enter a number within the range")
#     else:
#         print("Enter a valid number")





















# import random


# ans=random.randint(1,100)


# guess=int(input("GUess the numebr between 1 and 100: "))
# if guess<ans:
#     print("Too low!")
# elif guess>ans:
#     print("Too high!")
# elif guess==ans:
#     print("you guessed the number")

# def check(answer):
#     try:
#         int(answer)
#         return True
#     except ValueError:
#         return False
    
# print(check(5))
# print(check('a'))