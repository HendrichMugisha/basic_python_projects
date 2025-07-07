#the player guesses a secret word selected randonly from a list of words in a text file 
import random

# word_list = ['packet', 'shop', 'wrist', 'habit', 'trustee', 'script', 'lump', 'lobby', 'belong', 'star', 'brave', 'church', 'presence', 'appetite', 'democratic', 'volunteer', 'crown', 'insight', 'encourage', 'exploit', 'design', 'judicial', 'layout', 'photograph', 'confession', "begin", 'accompany', 'rear', 'child', 'wound', 'chocolate']

# with open('words.txt', 'w') as f:
#     for i in word_list:
#         f.write(i)
#         f.write(' ')

#open file and read it
with open('words.txt', 'r') as f:
    file_content = f.read()
    #store the words in a list by splitting the file contents by spaces
    words_list = list(file_content.split(" "))[:-2]


#this is to print the dashed list as it is initially and also as it fills up
def print_dashed_list(dashed_list):
    for i in dashed_list:
        print(i, end=' ')

#picking a secret random word
# secret_word = random.choice(words_list)
secret_word = random.choice(words_list)
# print(secret_word)

#initially creating and printing an empty dashed list with the same dashes as the secret word
dashed_list = []
for i in secret_word:
    dashed_list.append('_')
print_dashed_list(dashed_list)

#adjusting the number of trials(count) to match the specific secret word picked
if len(secret_word)<6:
    count = 6
else:
    count = len(secret_word)

#loop to do the thing
while count > 0:
    user_guess = input("\nEnter a letter: ") #user enters a their guess

    #checking if the user guess is in secret word to determine good or bad guesses

# the code has been altered to take care of words with multiple occurences of the same letter

    if user_guess in secret_word:   
        #creating list to store the indices at which the guessed letter might occur in the secret word
        required_indices = []
        print("Good Guess")

        #loop to count record the indices at which the correctly  guessed digit appears in the secret word
        for i in range(len(secret_word)):
            if user_guess == secret_word[i]:
                required_indices.append(i)
        # print(required_indices) 

        #loop to check the required indeces of the dashed list
        for index in required_indices:
            if dashed_list[index] == '_':
                #the guessed letter only replaces a dash
                dashed_list[index] = user_guess
                print_dashed_list(dashed_list)
                break
            else:
                #if there is no dash at the picked index, it means the letter has already been replaces, the loop simply picks the next required index
                continue

        if dashed_list == list(secret_word): #if the dashed list is finally same as the secret word, win win!
            print("\nYou guessed the word!")
            break
        else:
            print(f"\nYou have {count} remaining attempts! ")
        continue

        
    #word nor present, reduce number of remaining trials
    else:
        print("Wrong guess")
        count-=1
        if count > 0:
            print(f"\nYou have {count} remaining attempts! ")
        else:
            print(f"You failed! The word is {secret_word}")

