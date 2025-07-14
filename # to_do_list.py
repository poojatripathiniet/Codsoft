# to_do_list.py

todo_list = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Done")
    print("6. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks found.")
    else:
        for idx, task in enumerate(todo_list, start=1):
            status = "✔ Done" if task["done"] else "❌ Pending"
            print(f"{idx}. {task['task']} [{status}]")

def add_task():
    task = input("Enter the task: ")
    todo_list.append({"task": task, "done": False})
    print("Task added successfully.")

def update_task():
    view_tasks()
    try:
        index = int(input("Enter the task number to update: ")) - 1
        if 0 <= index < len(todo_list):
            new_task = input("Enter the new task: ")
            todo_list[index]["task"] = new_task
            print("Task updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def delete_task():
    view_tasks()
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(todo_list):
            removed = todo_list.pop(index)
            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def mark_done():
    view_tasks()
    try:
        index = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= index < len(todo_list):
            todo_list[index]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        mark_done()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")