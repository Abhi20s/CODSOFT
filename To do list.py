def display_tasks(tasks):
    print("\nTasks:")
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks):
            status = "Done" if task["done"] else "Not Done"
            print(f"{index + 1}. {task['task']} - {status}")

def main():
    tasks = []

    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Update Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                task_name = input("Enter the task: ")
                tasks.append({"task": task_name, "done": False})
                print("Task added!")
            except Exception as e:
                print(f"An error occurred: {e}")

        elif choice == '2':
            display_tasks(tasks)

        elif choice == '3':
            try:
                task_index = int(input("Enter the task number to mark as done: ")) - 1
                if 0 <= task_index < len(tasks):
                    tasks[task_index]["done"] = True
                    print("Task marked as done!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '4':
            try:
                task_index = int(input("Enter the task number to update: ")) - 1
                if 0 <= task_index < len(tasks):
                    new_task_name = input("Enter the new task description: ")
                    tasks[task_index]["task"] = new_task_name
                    print("Task updated!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '5':
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()