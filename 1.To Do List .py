# TASK-1-CODSOFT

'''
A To-Do List application is a useful project that helps users manage
and organize their tasks efficiently. This project aims to create a
command-line or GUI-based application using Python, allowing
users to create, update, and track their to-do lists
'''

# Function for displaying the Tasks

def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Update Task")
    print("4. Mark Task as Done")
    print("5. Exit")

# Funnction for the input of task from User

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    print(f'Task "{task}" added.')

# Function for Displaying the Overall Tasks

def list_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Pending"
            print(f"{i}. {task['task']} - {status}")

# Function for the updation of existing tasks 

def update_task(tasks):
    list_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Enter the task number to update: ")) - 1
            if 0 <= task_number < len(tasks):
                new_task = input("Enter the new task description: ")
                tasks[task_number]["task"] = new_task
                print(f'Task {task_number + 1} updated to "{new_task}".')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Function for marking the Tasks which are done

def mark_task_done(tasks):
    list_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_number < len(tasks):
                tasks[task_number]["done"] = True
                print(f'Task "{tasks[task_number]["task"]}" marked as done.')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Todo Fn for Selecting the choice of user 

def Todo():
    tasks = []

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            mark_task_done(tasks)
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    Todo()
