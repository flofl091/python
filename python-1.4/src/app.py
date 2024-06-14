# TO DO LIST - Version 1.4


class ToDoListApp:
    def __init__(self):
        self.tasks = []  # Liste pour stocker les tâches

    def add_task(self, name, urgency, date, time):
        if name:
            task = f"{name}"
            if urgency:
                task += f" - {urgency}"
            if date != "01/01/2020":
                task += f" - {date}"
            if time != "00h00":
                task += f" - {time}"
            self.tasks.append(task)
        else:
            raise ValueError("Task name cannot be empty")

    def delete_task(self, index):
        del self.tasks[index]

    def modify_task(self, index, new_task):
        self.tasks[index] = new_task

    def sort_tasks_by_name(self):
        self.tasks.sort()

    def sort_tasks_by_urgency(self):
        self.tasks.sort(key=lambda x: x.split(" ")[-1])

    def show_task_details(self, index):
        return self.tasks[index]
