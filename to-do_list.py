import os

TODO_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        print("Your To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def main():
    tasks = load_tasks()

    while True:
        print("\nOptions: [add] [view] [remove] [exit]")
        choice = input("What do you wanna do? ").strip().lower()

        if choice == "add":
            new_task = input("Enter your task: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print("Task added!")

        elif choice == "view":
            show_tasks(tasks)

        elif choice == "remove":
            show_tasks(tasks)
            try:
                index = int(input("Task number to delete: ")) - 1
                removed = tasks.pop(index)
                save_tasks(tasks)
                print(f"Removed: {removed}")
            except (ValueError, IndexError):
                print("Invalid task number!")

        elif choice == "exit":
            print("Your list is saved.")
            break

        else:
            print("I didn’t get that.")

if __name__ == "__main__":
    main()
