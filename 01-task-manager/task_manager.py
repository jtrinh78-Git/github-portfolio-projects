tasks = []

while True:
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        new_task = input("Enter a new task: ")
        tasks.append(new_task)

    elif choice == "2":
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")

    elif choice == "3":
        if tasks:
            remove_number = input("Enter task number to remove: ")

            if remove_number.isdigit():
                remove_number = int(remove_number)

                if 1 <= remove_number <= len(tasks):
                    tasks.pop(remove_number - 1)
                else:
                    print("Invalid task number.")
            else:
                print("Please enter a number.")
        else:
            print("No tasks to remove.")

    elif choice == "4":
        break

    else:
        print("Invalid choice. Please choose 1-4.")