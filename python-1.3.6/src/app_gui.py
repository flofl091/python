# TO DO LIST - Version 1.3.6

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
from tkcalendar import DateEntry
import datetime
import csv

class ToDoListGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("To-Do List")
        self.geometry("450x750")

        self.tasks = []
        self.notifications = []

        # Set up the UI components
        self.create_widgets()

        # Start the notification check loop
        self.check_notifications()

    def create_widgets(self):
        # Title Label
        self.title_label = ctk.CTkLabel(self, text="Ma Liste de Tâches", font=("Arial", 24))
        self.title_label.pack(pady=20)

        # Frame pour les boutons Ajouter et Supprimer Tâche
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=10)

        # Bouton Ajouter Tâche
        self.add_task_button = ctk.CTkButton(self.button_frame, text="Ajouter une tâche", command=self.open_add_task_window)
        self.add_task_button.pack(side=tk.LEFT, padx=5)

        # Bouton Supprimer Tâche
        self.delete_task_button = ctk.CTkButton(self.button_frame, text="Supprimer la tâche", command=self.delete_task)
        self.delete_task_button.pack(side=tk.LEFT, padx=5)

        # Frame pour les boutons Sauvegarder et Charger Tâches
        self.save_load_frame = ctk.CTkFrame(self)
        self.save_load_frame.pack(pady=10)

        # Bouton Sauvegarder Tâches
        self.save_tasks_button = ctk.CTkButton(self.save_load_frame, text="Sauvegarder les tâches", command=self.save_tasks)
        self.save_tasks_button.pack(side=tk.LEFT, padx=5)

        # Bouton Charger Tâches
        self.load_tasks_button = ctk.CTkButton(self.save_load_frame, text="Charger les tâches", command=self.load_tasks)
        self.load_tasks_button.pack(side=tk.LEFT, padx=5)

        # Frame pour Trier et Rechercher
        self.sort_search_frame = ctk.CTkFrame(self)
        self.sort_search_frame.pack(pady=10, fill=tk.X)

        # Menu déroulant pour le tri
        self.sort_var = tk.StringVar(value="Trier par")
        self.sort_menu = ctk.CTkOptionMenu(self.sort_search_frame, variable=self.sort_var, values=["Priorité", "Nom", "Date", "Personne"], command=self.sort_tasks)
        self.sort_menu.configure(width=80)
        self.sort_menu.pack(side=tk.LEFT, padx=5)

        # Entrée de recherche
        self.search_var = tk.StringVar()
        self.search_entry = ctk.CTkEntry(self.sort_search_frame, textvariable=self.search_var, width=300, placeholder_text="Rechercher...")
        self.search_entry.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        self.search_entry.bind("<KeyRelease>", self.search_tasks)

        # Liste des tâches (utilisation de Listbox de tkinter)
        self.task_listbox = tk.Listbox(self, width=48, height=25, font=("Arial", 14))
        self.task_listbox.pack(pady=20)
        self.task_listbox.bind("<Double-1>", self.open_edit_task_window)

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
        self.task_window.geometry("450x600")

        # Entrée pour le nom de la tâche
        self.task_name_label = ctk.CTkLabel(self.task_window, text="Nom")
        self.task_name_label.pack(pady=10)
        self.task_name_entry = ctk.CTkEntry(self.task_window, width=300)
        self.task_name_entry.pack(pady=10)

        # Sélection de priorité
        self.priority_label = ctk.CTkLabel(self.task_window, text="Priorité")
        self.priority_label.pack(pady=10)
        self.priority_var = tk.StringVar(value="Normal")
        self.priority_menu = ctk.CTkOptionMenu(self.task_window, variable=self.priority_var, values=["Bas", "Normal", "Élevé"])
        self.priority_menu.pack(pady=10)

        # Sélection de la date
        self.date_label = ctk.CTkLabel(self.task_window, text="Date")
        self.date_label.pack(pady=10)
        self.date_entry = DateEntry(self.task_window, width=16, background='lightblue', foreground='black', borderwidth=2, date_pattern="mm/dd/y")
        self.date_entry.pack(pady=10)

        # Frame pour l'heure (côte à côte avec les minutes)
        self.time_frame = ctk.CTkFrame(self.task_window)
        self.time_frame.pack(pady=20)

        # Label et Menu déroulant pour l'heure
        self.time_label = ctk.CTkLabel(self.time_frame, text="Heure")
        self.time_label.pack(side=tk.LEFT, padx=5)
        self.time_hour_var = tk.StringVar(value="08")  # Heure par défaut
        self.time_hour_menu = ctk.CTkOptionMenu(self.time_frame, variable=self.time_hour_var, values=[f"{i:02d}" for i in range(0, 24)])
        self.time_hour_menu.pack(side=tk.LEFT, padx=5)

        # Label et Menu déroulant pour les minutes
        self.minutes_label = ctk.CTkLabel(self.time_frame, text="")
        self.minutes_label.pack(side=tk.RIGHT, padx=0)
        self.time_minute_var = tk.StringVar(value="00")  # Minutes par défaut
        self.time_minute_menu = ctk.CTkOptionMenu(self.time_frame, variable=self.time_minute_var, values=[f"{i:02d}" for i in range(0, 60, 5)])
        self.time_minute_menu.pack(side=tk.RIGHT, padx=0)

        # Assignation à une personne
        self.person_label = ctk.CTkLabel(self.task_window, text="Assigné à")
        self.person_label.pack(pady=10)
        self.person_var = tk.StringVar(value="")
        self.person_menu = ctk.CTkOptionMenu(self.task_window, variable=self.person_var, values=["","Jerome", "Kevin", "Florian", "Julien"])
        self.person_menu.pack(pady=10)

        # Bouton Ajouter/Modifier Tâche dans la nouvelle fenêtre
        if task_details:
            self.task_name_entry.insert(0, task_details[0])
            self.priority_var.set(task_details[1])
            self.date_entry.set_date(datetime.datetime.strptime(task_details[2], "%m/%d/%y"))
            self.time_hour_var.set(task_details[3].split(":")[0])
            self.time_minute_var.set(task_details[3].split(":")[1])
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
        time = f"{self.time_hour_var.get()}:{self.time_minute_var.get()}"
        person = self.person_var.get()

        if task_name and priority and date and time:
            task = f"{task_name} - {priority} - {date} - {time}"
            if person:
                task += f" - {person}"
            self.tasks.append(task)
            self.update_task_listbox()
            self.schedule_notification(task)
            self.task_window.destroy()
        else:
            messagebox.showwarning("Erreur de saisie", "Remplissez tous les champs.")

    def edit_task(self, task_index):
        task_name = self.task_name_entry.get()
        priority = self.priority_var.get()
        date = self.date_entry.get_date().strftime("%m/%d/%y")
        time = f"{self.time_hour_var.get()}:{self.time_minute_var.get()}"
        person = self.person_var.get()

        if task_name and priority and date and time:
            task = f"{task_name} - {priority} - {date} - {time}"
            if person:
                task += f" - {person}"
            self.tasks[task_index] = task
            self.update_task_listbox()
            self.schedule_notification(task)
            self.task_window.destroy()
        else:
                messagebox.showwarning("Erreur de saisie", "Remplissez tous les champs.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Erreur de sélection", "Sélectionnez une tâche à supprimer.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def search_tasks(self, event):
        search_term = self.search_var.get().lower()
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_name = task.split(" - ")[0].lower()
            if search_term in task_name:
                self.task_listbox.insert(tk.END, task)

    def sort_tasks(self, selected_sort):
        if selected_sort == "Priorité":
            priority_order = {"Élevé": 0, "Normal": 1, "Bas": 2}
            self.tasks.sort(key=lambda x: priority_order[x.split(" - ")[1]])
        elif selected_sort == "Nom":
            self.tasks.sort(key=lambda x: x.split(" - ")[0])
        elif selected_sort == "Date":
            self.tasks.sort(key=lambda x: datetime.datetime.strptime(x.split(" - ")[2], "%m/%d/%y"))
        elif selected_sort == "Personne":
            self.tasks.sort(key=lambda x: x.split(" - ")[-1] if x.count(" - ") == 4 else "")
        self.update_task_listbox()

    def save_tasks(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Fichiers CSV", "*.csv")])
        if file_path:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                for task in self.tasks:
                    writer.writerow(task.split(" - "))
            messagebox.showinfo("Succès", "Les tâches ont été sauvegardées avec succès.")

    def load_tasks(self):
        file_path = filedialog.askopenfilename(filetypes=[("Fichiers CSV", "*.csv")])
        if file_path:
            with open(file_path, mode='r') as file:
                reader = csv.reader(file)
                self.tasks = [" - ".join(row) for row in reader]
            self.update_task_listbox()
            messagebox.showinfo("Succès", "Les tâches ont été chargées avec succès.")

    def schedule_notification(self, task):
        task_details = task.split(" - ")
        task_time_str = f"{task_details[2]} {task_details[3]}"
        task_time = datetime.datetime.strptime(task_time_str, "%m/%d/%y %H:%M")
        notify_time = task_time - datetime.timedelta(minutes=10)
        self.notifications.append((notify_time, task))

    def check_notifications(self):
        current_time = datetime.datetime.now()
        for notify_time, task in self.notifications[:]:
            if current_time >= notify_time:
                self.notifications.remove((notify_time, task))
                messagebox.showinfo("Notification", f"Vous avez une tâche à faire dans 10 minutes :\n{task}")
        self.after(60000, self.check_notifications)  # Vérifier toutes les minutes