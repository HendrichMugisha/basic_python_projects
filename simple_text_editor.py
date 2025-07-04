# program to allow users to open an existing file or create a new one, edit content and hen save the changes typing the save command
def write_content(file_name):
   with open(file_name, 'w') as f:
        f.write(input("Enter your text (type 'SAVE' on a new line to save and exit): "))

def display_or_write(choice,file_name):
    if choice == '1':
        with open(file_name, 'r') as f:
            file_content = f.read()
            print(file_content)
    elif choice == '2':
        write_content(file_name)

while True:
    file_name = input("Enter the filename to open or create (.txt format): ")
    # print(type(file_name))
    try: 
        with open(file_name, 'r') as f:
            choice = input("file found! Enter 1 to display file content, Enter 2 to write to file: ")
            display_or_write(choice, file_name)
    except FileNotFoundError:
        user_choice = input(f"{file_name} not found! creating a new file\nWould you like to create a new file {file_name}? (y/n): ").lower()
        if user_choice =='y':
            write_content(file_name)
        else:
            print("program terminated!")
            break
    
    
