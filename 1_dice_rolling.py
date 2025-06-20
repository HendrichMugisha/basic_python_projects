#progam to generate 2 random numbers and insert them into a turple
import random

#take the response from the user
i=1
while i>=0:
    response=input("Roll the dice? (y/n): ")

    #add input("roll the dice").lower()
    if response=='y' or response== 'Y':
        result=(random.randint(1,6), random.randint(1,6))
        print(result)
    elif response=='n' or response== 'N':
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")
    i+=1
