

from app import ToDoListApp

class ToDoListCLI(ToDoListApp):
    def __init__(self):
        self.tasks = []
        self.display_menu()

    def display_menu(self):
        print("1. Add Task")
        print("2. Show Task Details")
        print("3. Modify Task")
        print("4. Delete Task")
        print("5. Exit")

    def add_task(self, name, urgency, date, time):
        if name:
            task = f"{name}"
            if urgency:
                task += f" - Urgency {urgency}"
            if date:
                task += f" - Date: {date}"
            if time:
                task += f" - Time: {time}"
            self.tasks.append(task)
        else:
            print("Please enter the task name.")

    def show_task_details(self):
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def modify_task(self):
        self.show_task_details()
        index = int(input("Enter the index of the task you want to modify: ")) - 1
        new_task = input("Enter the new task: ")
        self.tasks[index] = new_task

    def delete_task(self):
        self.show_task_details()
        index = int(input("Enter the index of the task you want to delete: ")) - 1
        del self.tasks[index]
