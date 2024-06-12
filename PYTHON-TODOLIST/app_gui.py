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
        self.sort_menu = ctk.CTkOptionMenu(self, variable=self.sort_var, values=["Priorité", "Nom", "Date"], command=self.sort_tasks)
        self.sort_menu.pack(pady=10)

        # Task Listbox (using tkinter Listbox)
        self.task_listbox = tk.Listbox(self, width=48, height=25, font=("Arial", 14))
        self.task_listbox.pack(pady=20)

        # Delete Task Button
        self.delete_task_button = ctk.CTkButton(self, text="Supprimer la tâche", command=self.delete_task)
        self.delete_task_button.pack(pady=10)

    def open_add_task_window(self):
        self.add_task_window = ctk.CTkToplevel(self)
        self.add_task_window.title("Ajouter la tâche")
        self.add_task_window.geometry("400x500")

        # Task Name Entry
        self.task_name_label = ctk.CTkLabel(self.add_task_window, text="Nom")
        self.task_name_label.pack(pady=10)
        self.task_name_entry = ctk.CTkEntry(self.add_task_window, width=300)
        self.task_name_entry.pack(pady=10)

        # Priority Selection
        self.priority_label = ctk.CTkLabel(self.add_task_window, text="Priorité")
        self.priority_label.pack(pady=10)
        self.priority_var = tk.StringVar(value="Normal")
        self.priority_menu = ctk.CTkOptionMenu(self.add_task_window, variable=self.priority_var, values=["Bas", "Normal", "Elevé"])
        self.priority_menu.pack(pady=10)

        # Date Entry
        self.date_label = ctk.CTkLabel(self.add_task_window, text="Date")
        self.date_label.pack(pady=10)
        self.date_entry = DateEntry(self.add_task_window, width=16, background='lightblue', foreground='black', borderwidth=2)
        self.date_entry.pack(pady=10)

        # Time Entry
        self.time_label = ctk.CTkLabel(self.add_task_window, text="Heure (HH:MM)")
        self.time_label.pack(pady=10)
        self.time_entry = ctk.CTkEntry(self.add_task_window, width=300)
        self.time_entry.pack(pady=10)

        # Add Task Button in the new window
        self.add_task_confirm_button = ctk.CTkButton(self.add_task_window, text="Ajouter la tâche", command=self.add_task)
        self.add_task_confirm_button.pack(pady=20)

    def add_task(self):
        task_name = self.task_name_entry.get()
        priority = self.priority_var.get()
        date = self.date_entry.get_date()
        time = self.time_entry.get()

        if task_name and priority and date and time:
            task = f"{task_name} - {priority} - {date} - {time}"
            self.tasks.append(task)
            self.update_task_listbox()
            self.add_task_window.destroy()
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
            self.tasks.sort(key=lambda x: x.split(" - ")[1])
        elif selected_sort == "Nom":
            self.tasks.sort(key=lambda x: x.split(" - ")[0])
        elif selected_sort == "Date":
            self.tasks.sort(key=lambda x: datetime.datetime.strptime(x.split(" - ")[2], "%d/%m/%y"))
