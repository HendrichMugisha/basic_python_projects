#the player guesses a secret word selected randonly from a list of words in a text file 

word_list = ['packet', 'shop', 'wrist', 'habit', 'trustee', 'script', 'lump', 'lobby', 'belong', 'star', 'brave', 'church', 'presence', 'appetite', 'democratic', 'volunteer', 'crown', 'insight', 'encourage', 'exploit', 'design', 'judicial', 'layout', 'photograph', 'confession', "begin", 'accompany', 'rear', 'child', 'wound', 'chocolate']

with open('words.txt', 'w') as f:
    for i in word_list:
        f.write(i)
        f.write(' ')
words_list = []

with open('words.txt', 'r') as f:
    file_content = f.read()

count = len(file_content)
while count>0:
    with open('words.txt', 'r') as f:
        word = 'w'

        for i in range(len(file_content)):
            if file_content[i] != " ":
                word+=file_content[i]
            else:
                words_list.append(word[1:])
                pass
                continue
    count-=1
print(len(words_list))
print(len(word_list))
    # character = file_content[i]
        


    



def print_dashed_list(dashed_list):
    for i in dashed_list:
        print(i, end=' ')

secret_word = 'word'
dashed_list = []
for i in secret_word:
    dashed_list.append('_')
print_dashed_list(dashed_list)
if len(secret_word)<6:
    count = 6
else:
    count = len(secret_word)

while count > 0:
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

