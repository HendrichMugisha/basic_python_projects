#program to generate a random password based on user_specified criteria
import random

ascii_characters = [chr(i) for i in range(128)]
upper_case_letters = ascii_characters[65:91]
numbers = ascii_characters[48:58]
special_chars = ascii_characters[33:48] + ascii_characters[58:65]


def questions():
    length = int(input("Enter password length: "))
    upper_choice = input("Include uppercase letter? (y/n): ")
    nums_choice = input("Include numbers? (y/n): ")
    special_choice = input("Include special characters? (y/n): ")

    return length, upper_choice, nums_choice, special_choice

user_choices = questions() 
length = user_choices[0]
final_list = ascii_characters[97:123]
if user_choices[1]=='y' and user_choices[2] == 'y' and user_choices[3] == 'y':
    final_list += upper_case_letters + numbers + special_chars

elif user_choices[1]=='y' and user_choices[2] == 'y' and user_choices[3] == 'n':
    final_list += upper_case_letters + numbers

elif user_choices[1]=='y' and user_choices[2] == 'n' and user_choices[3] == 'n':
    final_list += upper_case_letters

elif user_choices[1]=='n' and user_choices[2] == 'n' and user_choices[3] == 'n':
    final_list = final_list

elif user_choices[1]=='n' and user_choices[2] == 'n' and user_choices[3] == 'y':
    final_list += special_chars

elif user_choices[1]=='n' and user_choices[2] == 'y' and user_choices[3] == '':
    final_list += numbers 


elif user_choices[1]=='y' and user_choices[2] == 'n' and user_choices[3] == 'y':
    final_list += upper_case_letters + special_chars

password= 'p'
for character in random.sample(final_list, length):
    password+=character

print(f"Generated password: {password[1:]}")
