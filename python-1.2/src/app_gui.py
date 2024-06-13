import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import datetime

class ToDoListGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("To-Do List")
        self.geometry("400x700")

        self.tasks = []

        # Set up the UI components
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = ctk.CTkLabel(self, text="My To-Do List", font=("Arial", 24))
        self.title_label.pack(pady=20)

        # Add Task Button
        self.add_task_button = ctk.CTkButton(self, text="Ajouter une tâche", command=self.open_add_task_window)
        self.add_task_button.pack(pady=10)

        # Sort Dropdown Menu
        self.sort_var = tk.StringVar(value="Trier par...")
        self.sort_menu = ctk.CTkOptionMenu(self, variable=self.sort_var, values=["Priorité", "Nom", "Date", "Personne"], command=self.sort_tasks)
        self.sort_menu.pack(pady=10)

        # Task Listbox (using tkinter Listbox)
        self.task_listbox = tk.Listbox(self, width=48, height=25, font=("Arial", 14))
        self.task_listbox.pack(pady=20)
        self.task_listbox.bind("<Double-1>", self.open_edit_task_window)

        # Delete Task Button
        self.delete_task_button = ctk.CTkButton(self, text="Supprimer la tâche", command=self.delete_task)
        self.delete_task_button.pack(pady=10)

    def open_add_task_window(self):
        self.open_task_window()

    def open_edit_task_window(self, event):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            task_details = task.split(" - ")
            self.open_task_window(task_details, selected_task_index[0])

    def open_task_window(self, task_details=None, task_index=None):
        self.task_window = ctk.CTkToplevel(self)
        self.task_window.title("Ajouter/Modifier la tâche")
        self.task_window.geometry("400x550")

        # Task Name Entry
        self.task_name_label = ctk.CTkLabel(self.task_window, text="Nom")
        self.task_name_label.pack(pady=10)
        self.task_name_entry = ctk.CTkEntry(self.task_window, width=300)
        self.task_name_entry.pack(pady=10)

        # Priority Selection
        self.priority_label = ctk.CTkLabel(self.task_window, text="Priorité")
        self.priority_label.pack(pady=10)
        self.priority_var = tk.StringVar(value="Normal")
        self.priority_menu = ctk.CTkOptionMenu(self.task_window, variable=self.priority_var, values=["Bas", "Normal", "Elevé"])
        self.priority_menu.pack(pady=10)

        # Date Entry
        self.date_label = ctk.CTkLabel(self.task_window, text="Date")
        self.date_label.pack(pady=10)
        self.date_entry = DateEntry(self.task_window, width=16, background='lightblue', foreground='black', borderwidth=2, date_pattern="mm/dd/y")
        self.date_entry.pack(pady=10)

        # Time Entry
        self.time_label = ctk.CTkLabel(self.task_window, text="Heure (HH:MM)")
        self.time_label.pack(pady=10)
        self.time_entry = ctk.CTkEntry(self.task_window, width=300)
        self.time_entry.pack(pady=10)

        # Person Assignment
        self.person_label = ctk.CTkLabel(self.task_window, text="Assigné à")
        self.person_label.pack(pady=10)
        self.person_var = tk.StringVar(value="")
        self.person_menu = ctk.CTkOptionMenu(self.task_window, variable=self.person_var, values=["Jerome", "Kevin", "Florian", "Julien"])
        self.person_menu.pack(pady=10)

        # Add/Edit Task Button in the new window
        if task_details:
            self.task_name_entry.insert(0, task_details[0])
            self.priority_var.set(task_details[1])
            self.date_entry.set_date(datetime.datetime.strptime(task_details[2], "%m/%d/%y"))
            self.time_entry.insert(0, task_details[3])
            if len(task_details) > 4:
                self.person_var.set(task_details[4])
            self.task_confirm_button = ctk.CTkButton(self.task_window, text="Modifier la tâche", command=lambda: self.edit_task(task_index))
        else:
            self.task_confirm_button = ctk.CTkButton(self.task_window, text="Ajouter la tâche", command=self.add_task)
        self.task_confirm_button.pack(pady=20)

    def add_task(self):
        task_name = self.task_name_entry.get()
        priority = self.priority_var.get()
        date = self.date_entry.get_date().strftime("%m/%d/%y")
        time = self.time_entry.get()
        person = self.person_var.get()

        if task_name and priority and date and time:
            task = f"{task_name} - {priority} - {date} - {time}"
            if person:
                task += f" - {person}"
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_window.destroy()
        else:
            messagebox.showwarning("Input Error", "Remplir tous les champs.")

    def edit_task(self, task_index):
        task_name = self.task_name_entry.get()
        priority = self.priority_var.get()
        date = self.date_entry.get_date().strftime("%m/%d/%y")
        time = self.time_entry.get()
        person = self.person_var.get()

        if task_name and priority and date and time:
            task = f"{task_name} - {priority} - {date} - {time}"
            if person:
                task += f" - {person}"
            self.tasks[task_index] = task
            self.update_task_listbox()
            self.task_window.destroy()
        else:
            messagebox.showwarning("Input Error", "Remplir tous les champs.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Selection Error", "Sélectionner une tâche à supprimer.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def sort_tasks(self, selected_sort):
        if selected_sort == "Priorité":
            priority_order = {"Elevé": 0, "Normal": 1, "Bas": 2}
            self.tasks.sort(key=lambda x: priority_order[x.split(" - ")[1]])
        elif selected_sort == "Nom":
            self.tasks.sort(key=lambda x: x.split(" - ")[0])
        elif selected_sort == "Date":
            self.tasks.sort(key=lambda x: datetime.datetime.strptime(x.split(" - ")[2], "%m/%d/%y"))
        elif selected_sort == "Personne":
            self.tasks.sort(key=lambda x: x.split(" - ")[-1] if x.count(" - ") == 4 else "")
        self.update_task_listbox()

if __name__ == "__main__":
    app = ToDoListGUI()
    app.mainloop()
