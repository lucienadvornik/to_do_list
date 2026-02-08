########## Requirements --> actions ##########
## 1. Show tasks --> show_task()
## 2. Add task --> add_task()
## 3. Complete task --> complete_task()
## 4. Exit --> no function needed
## All in menu shown to user --> show_menu

########## Libraries ##########
import uuid # generating a random unique identifier


########## Set the source file ##########
file = 'tasks.txt'


########## 1) SHOW TASKS ##########

def show_tasks():
    try:
        stream = open('tasks.txt', 'r')   # showing tasks for read
        tasks = stream.readlines()        # returns list of lines
        for line in tasks:
            print(line.strip())
        stream.close()
    except Exception as e:
        print('An error occurred: ', e)

# if __name__ == '__main__':
#     show_tasks()


########## 2) ADD TASK ##########

def add_task():
    print('\n**ADD TASKS**')
    task = input('What is the task? ') # user inputs
    deadline = input('What is the deadline? ')
    counter = 0
    try:
        # find out how many tasks are there
        try:
            stream = open('tasks.txt', 'r')
            counter = (len(stream.readlines())-3) # 3 rows are title
            stream.close()
        except FileNotFoundError:
            counter = 0

        counter += 1 
        # add task to list: id | task | deadline

        # random ID by using uuid4
        # stream.write('|'+ str(uuid.uuid4())[0:6] + '|' + task + '|'+ deadline+ '|'+ '\n') 
        
        # ID as a counter
        stream = open('tasks.txt', 'a')
        stream.write('|   '+ str(counter) + '  |' + task + ' |'+ deadline+ '|'+ '\n') 
        stream.close()
    except Exception as e:
        print('Error while adding a task:', e)


########## 3) COMPLETE TASK ##########

def complete_task():
    print('\n**COMPLETE TASK**')
    show_tasks()

    try:
        stream = open('tasks.txt', 'r')
        lines = stream.readlines()
        stream.close()
    except FileNotFoundError:
        print('No tasks to complete!')
        return

    if len(lines) == 0:
        print('No tasks to complete!')
        return

    id_to_delete = input('Enter ID to complete: ').strip()

    stream = open('tasks.txt', 'w')
    for line in lines:
        parts = line.split('|') # because of spaces in the ID field

        if len(parts) >= 3:
            line_id = parts[1].strip()
            if line_id != id_to_delete:
                stream.write(line)
        else:
            stream.write(line)

    stream.close()
    print('Task completed!\n')


########## MAIN LOOP (menu display) ##########
# when user chooses 1 --> show tasks, when 2 --> add task, ...
# must be in function show_menu


def show_menu(): # function for menu with user input
    width = 28
    while True: 
        print('_' * width)  # upper line 
        print('| ====== TO DO LIST ====== '.ljust(width - 1) + '|')

        print('| [1] Show tasks '.ljust(width - 1) + '|') # adds spaces to right until 19 chars
        print('| [2] Add task '.ljust(width - 1) + '|')
        print('| [3] Complete task '.ljust(width - 1) + '|')
        print('| [4] Exit '.ljust(width - 1) + '|')
        print('‾'*28) # bottom line

        choice = input('Your choice: ').strip()

        if choice == '1': # if user chooses 1
            show_tasks()
        elif choice == '2': # -//- 2
            add_task()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            print('Okay, bye!')  # will exit the choice
            break
        else:
            print('Enter a corrent number') # in case of wrong number
            
if __name__ == '__main__':
    show_menu()