'''
IMPROVEMENTS

- Recursive functions for bytesize and number of files
- List number of files in tabular format and display if they're a folder or
  file
- Improve menu: Return to menu page and clear os after each function
- Clean up with main() and module scripts
'''

import os

def list_current_working_directory():
    '''
    Prints the current working directory
    '''
    print('\n' + 'CWD: ' + (os.getcwd()))


def move_up():
    '''
    Moves up one directory in the file tree
    '''
    os.chdir('..')


def move_down():
    '''
    Moves down one directory based on user input
    '''

    new_directory = input('\nEnter directory: ')

    if os.path.exists(new_directory):    # Checking is the directory exists
        os.chdir(new_directory)    # Changing to the directory if it exists
    else:
        print('\nError - Directory not found')    # Error message if it doesn't


def print_number_of_files():
    '''
    Print the number of total items, files and folders in the current directory
    '''
    file_list = os.listdir(os.getcwd())    # Create a list of items in the cwd

    folder_count = 0
    file_count = 0

    for i in file_list:    # Iterating over the list of items
        if os.path.isfile(i):
            file_count += 1
        else:
            folder_count += 1

    print(f'\nNumber of items in current directory: {len(file_list)}')
    print(f'\nNumber of folders: {folder_count}')
    print(f'\nNumber of files: {file_count}')


def print_number_of_bytes():
    '''
    Print the total size of the cwd
    '''
    byte_count = 0
    item_list = os.listdir(os.getcwd())    # Create a list of items in the cwd

    # Iterate over the items and add their bytesize to the counter:
    for i in item_list:
        byte_count += os.path.getsize(i)

    print(f'\nNumber of bytes in current directory: {byte_count}')


def filename_search():
    '''
    Searth the cwd for items matching a user's input, then printing the names of
    any such items
    '''

    filename = input('\nEnter filename: ').strip()
    items = []    # Empty list to contain files containing the user input
    item_list = os.listdir(os.getcwd())    # Create a list of files in the cwd

    # Iterate over the files in the cwd and check if their names contain the
    # user input:
    for i in item_list:
        if filename in i:
            items.append(i)

    # Print results of the search to the user
    if len(items) > 0:
        print(f"\nFiles found matching '{filename}':\n")
        for i in items:
            print(i)
    else:
        print(f"\nNo files found matching '{filename}'")


def list_files():    # List all the items in the cwd
    print('\ITEMS: \n')
    for i in os.listdir(os.getcwd()):
        print(i)


menu = '''
1  List the current working directory
2  Move up
3  Move down
4  Number of items in current working directory
5  List all the items in the current directory
6  Size of current working directory
7  Search by item name
8  Quit the program\
'''


# Main program logic

program_running = True

print(menu)

while program_running:
    
    print('\n' + os.getcwd() + '\n')
    user_choice = input('Enter a number: ').strip()

    if user_choice == '1':
        list_current_working_directory()

    elif user_choice == '2':
        move_up()

    elif user_choice == '3':
        move_down()

    elif user_choice == '4':
        print_number_of_files()

    elif user_choice == '5':
        list_files()

    elif user_choice == '6':
        print_number_of_bytes()

    elif user_choice == '7':
        filename_search()
    
    elif user_choice == '8':
        print('\nEXITING PROGRAM\n')
        program_running = False

    else:
        print('\nInvalid input')