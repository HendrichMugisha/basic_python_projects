import random

#generate trial number and check for any repeating digits; the secret number should not have any repeating digits
while True:
    trial_number=str(random.randint(1000,9999)) #convert generateed number to a string
    #we asssume that this is the secret number
    v=1 
    #loop for picking each digit in the string and prepare it for checking
    for i in range(len(trial_number)):
        digit=trial_number[i]
        #list comprehension to compare the picked digit with the rest of the string 
        if digit in list(trial_number)[i+1:]:
            v=2 #if found, we realise our assumption was wrong and break out of the loop 
            break
        else:
            continue #else if not found, we proceeed to pick the next digit 
            
    #If on exiting the inner checking loop, the value of v is still 1, we found the secret number. 
    if v==1:
        secret_number=trial_number
        break

#time to use the secret number
print(f'Secret number: {secret_number}')
print("I have generated a 4-digit number with unique digits. Try to guess it!")

while True:
    user_guess = input("Guess: ")
    #cows means the digit is present but in the wrong position // bulls means it is present in right position

    secret_number_list =list(secret_number)
    user_guess_list = list(user_guess)
    if len(user_guess_list) == len(secret_number_list):
        bulls=0
        cows=0
        #couting bulls
        for i in range(len(secret_number_list)):
            if secret_number_list[i] == user_guess_list[i]: #if the item and position is the same in both lists
                bulls+=1
            if user_guess_list[i] in secret_number_list: #if an item from the user_list simply exists in the secret list
                cows+=1
        if bulls==len(secret_number_list):
            print(f"You Guessed it! Its {secret_number} ")
            break
        else:
            if (bulls == 1) and (cows-bulls == 1):
                print(f"{cows-bulls} Cow, {bulls} Bull")
            elif bulls==1:
                print(f"{cows-bulls} Cows, {bulls} Bull")
            elif cows == 1:
                print(f"{cows-bulls} Cow, {bulls} Bulls")
            else:
                print(f"{cows-bulls} Cows, {bulls} Bulls")
    

