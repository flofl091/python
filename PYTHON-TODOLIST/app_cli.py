

from app import ToDoListApp

class ToDoListCLI(ToDoListApp):
    def __init__(self):
        super().__init__()
        self.display_menu()

    def display_menu(self):
        while True:
            print("\n1. Add Task")
            print("2. Show Task Details")
            print("3. Modify Task")
            print("4. Delete Task")
            print("5. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_task_cli()
            elif choice == "2":
                self.show_task_details_cli()
            elif choice == "3":
                self.modify_task_cli()
            elif choice == "4":
                self.delete_task_cli()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    def add_task_cli(self):
        name = input("Enter task name: ")
        urgency = input("Enter task urgency (!, !!, !!!): ")
        date = input("Enter task date (YYYY-MM-DD): ")
        time = input("Enter task time (HH:MM): ")
        self.add_task(name, urgency, date, time)

    def show_task_details_cli(self):
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def modify_task_cli(self):
        self.show_task_details_cli()
        index = int(input("Enter the index of the task you want to modify: ")) - 1
        new_task = input("Enter the new task: ")
        self.modify_task(index, new_task)

    def delete_task_cli(self):
        self.show_task_details_cli()
        index = int(input("Enter the index of the task you want to delete: ")) - 1
        self.delete_task(index)