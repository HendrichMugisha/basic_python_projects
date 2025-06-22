#program to allow user to add tasks, view the current list of tasks, and remove taks on completion

tasks_list=['workout', 'meditate', 'breakfast', 'study', 'sleep']
while True:
    try:
        user_choice=int(input('\vTodo List Menu:' \
                        '\n1. View Tasks\n2. Add a Task\n3. Remove a Task\n4. Exit' \
                        '\nEnter your choice: '))
        if user_choice not in [1,2,3,4]:
            pass
        elif user_choice==1:
            print("\nHere are your tasks:")
            for i in range(len(tasks_list)):
                print(f'{i+1}. {tasks_list[i]}')
        elif user_choice==2:
            new_task=input('Enter new task: ')
            tasks_list.append(new_task)
            print(f'Task {new_task} added!')
            print(tasks_list)
        elif user_choice==3:
            print(f"\nYou have {len(tasks_list)} pending tasks:")
            for i in range(len(tasks_list)):
                print(f'{i+1}. {tasks_list[i]}')
            try: 
                task_to_remove=int(input(f'Enter task to remove{1}-{len(tasks_list)}: '))
                tasks_list.remove(tasks_list[task_to_remove-1])
                print("task removed successfully!")
            except ValueError:
                print('Task not found!')
        elif user_choice==4:
            break
            
        
    except ValueError:
        print('Enter valid choice!')


            