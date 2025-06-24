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

