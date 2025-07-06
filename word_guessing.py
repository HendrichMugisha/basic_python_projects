#the player guesses a secret word selected randonly from a list of words in a text file 

def print_dashed_list(dashed_list):
    for i in dashed_list:
        print(i, end=' ')

secret_word = 'word'
dashed_list = []
for i in secret_word:
    dashed_list.append('_')
print_dashed_list(dashed_list)
count=6

while count>0:
    user_guess = input("\nEnter a letter: ")

    if user_guess in secret_word:
        print("Good Guess")
        for i in range(len(secret_word)):
            if user_guess == secret_word[i]:
                required_index = i
                break 
        dashed_list[required_index] = user_guess
        print_dashed_list(dashed_list)
        if dashed_list == list(secret_word):
            print("\nYou guessed the word!")
            break
        else:
            print(f"\nYou have {count} remaining attempts! ")
        continue
    else:
        print("Wrong guess")
        count-=1
        print(f"\nYou have {count} remaining attempts! ")

