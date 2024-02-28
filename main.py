'''
IMPROVEMENTS

- Recursive functions for bytesize and number of files
- List number of files in tabular format and display if they're a folder or
  file
- Improve menu: Return to menu page and clear os after each function
- Clean up with main() and module scripts
'''

import os

def print_current_working_directory():
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


def print_number_of_items():
    '''
    Print the number of total items, files and folders in the current directory
    '''
    item_list = os.listdir(os.getcwd())    # Create a list of items in the cwd

    folder_count = 0
    file_count = 0

    for i in item_list:    # Iterating over the list of items
        if os.path.isfile(i):
            file_count += 1
        else:
            folder_count += 1

    print(f'\nNumber of items in current directory: {len(item_list)}')
    print(f'\nNumber of folders: {folder_count}')
    print(f'\nNumber of files: {file_count}')


def print_recursive_number_of_items(dir_path):
    '''
    Return the total number of items both in the current working directory AND
    all subdirectories
    '''
    item_list = os.listdir(dir_path)    # Create a list of items in the cwd
    item_count = 0

    for item in item_list:    # Iterating over the list of items

        item_path = os.path.join(dir_path, item)

        if os.path.isfile(item_path):
            item_count += 1
        else:
            item_count += print_recursive_number_of_items(item_path)

    return item_count


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


def search():
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


def list_items():    # List all the items in the cwd
    print('\ITEMS: \n')
    for i in os.listdir(os.getcwd()):
        print(i)


menu = '''
1  List the current working directory
2  Move up
3  Move down
4  Number of items in current working directory (excl. subdirectories)
5  Number of items in current working directoy (incl. subdirectories)
6  List all the items in the current directory
7  Size of current working directory
8  Search
9  Quit the program\
'''


# Main program logic

program_running = True

print(menu)

while program_running:
    
    print('\n' + os.getcwd() + '\n')
    user_choice = input('Enter a number: ').strip()

    if user_choice == '1':
        print_current_working_directory()

    elif user_choice == '2':
        move_up()

    elif user_choice == '3':
        move_down()

    elif user_choice == '4':
        print_number_of_items()

    elif user_choice == '5':
        number_of_items = print_recursive_number_of_items(os.getcwd())
        print(f'Number of items in current working directory (incl.\
subdirectories): {number_of_items}')

    elif user_choice == '6':
        list_items()

    elif user_choice == '7':
        print_number_of_bytes()

    elif user_choice == '8':
        search()
    
    elif user_choice == '9':
        print('\nEXITING PROGRAM\n')
        program_running = False

    else:
        print('\nInvalid input')