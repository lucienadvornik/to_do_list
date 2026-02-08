########## Requirements ##########
## Show tasks
## Add tasks
## Delete (complete) tasks
## Exit

########## Libraries ##########
import uuid # generating a random unique identifier


########## UI (menu display) ##########
def show_menu():
    print('\n == TO DO LIST == ')
    print('[1] Show tasks')
    print('[2] Add task')
    print('[3] Complete task')
    print('[4] Exit')


########## Main applicaion loop (Program control flow) ##########
def main():
    while True:
        show_menu()
        choice = input("Your choice: ").strip() 
        if choice == "1":
            print("TODO: show tasks")
        elif choice == "2":
            print("TODO: add task")
        elif choice == "3":
            print("TODO: complete task")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()


########## Loading tasks from file ##########
file = 'tasks.txt'


########## Showing tasks ##########
