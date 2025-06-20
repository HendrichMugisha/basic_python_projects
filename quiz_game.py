#program where a player answers multiple choice questions

#use a dictionary to map each question to the list of options
questions_and_options={
    #The correct option is placed as the last option of the answer list
    'What is the capital city of France?': ['a: Paris', 'b: London', 'c: Rome', 'a'],
    'What is the largest planet in our solar system?': ['a: Earth', 'b: Jupiter', 'c: Mars', 'b']
}
#create a list with the dictionary keys alone
questions_list=list(questions_and_options.keys())

#deal with each key separately 
for i in range(len(questions_list)):
    #print the question by accessing the key from the dictionary
    print(f'Question {i+1}: {questions_list[i]}\n')
    #access the corresponding options for that question and add them to a list
    options_list=questions_and_options[questions_list[i]]
    #acces the list woith the correct options and print member at a time
    for i in range(len(options_list[:len(options_list)-1])):
         print()

# print(list(questions_dict.keys())[0])






# users_answer=input('Question 1: What is the capital city of france?\na) Paris\nb) London\nc)Rome\nYour answer: ')

# if users_answer== 'Paris':
#     print('Correct')







































# questions_and_answers={'What is the captial city of france?\n':''}