class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        print("Tasks:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
            print("Task added successfully!")

        elif choice == '2':
            todo_list.view_tasks()

        elif choice == '3':
            print("Exiting the To-Do List. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

