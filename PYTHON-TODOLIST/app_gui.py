

import tkinter as tk
from tkinter import messagebox
from app import ToDoListApp

class ToDoListGUI(ToDoListApp):
    def __init__(self):
        self.tasks = []  # Liste pour stocker les tâches
        self.create_gui()  # Appeler la fonction pour créer l'interface graphique

    def create_gui(self):
        # Créer la fenêtre principale
        self.root = tk.Tk()
        self.root.title("To-Do List")  # Titre de la fenêtre principale

        # Bouton "+" pour ajouter une tâche
        self.add_task_button = tk.Button(self.root, text="+", command=self.add_task_window)
        self.add_task_button.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=10)

        # Liste des tâches
        self.task_listbox = tk.Listbox(self.root, height=20, width=60)
        self.task_listbox.pack(pady=10, padx=10)

        # Lier la double-clic sur une tâche à la fonction pour afficher les détails
        self.task_listbox.bind("<Double-Button-1>", self.show_task_details)

        self.root.mainloop()  # Lancer la boucle principale pour afficher l'interface graphique

    def add_task_window(self):
        # Fonction pour afficher une fenêtre pour ajouter une tâche
        add_window = tk.Toplevel(self.root)  # Créer une nouvelle fenêtre
        add_window.title("Add Task")  # Titre de la fenêtre

        # Éléments de l'interface pour ajouter une tâche (labels, menus déroulants, bouton)
        tk.Label(add_window, text="Nom de la tâche:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        entry_nom = tk.Entry(add_window, width=30)
        entry_nom.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(add_window, text="Urgence:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        urgence_var = tk.StringVar(add_window)
        urgence_var.set("")  
        dropdown_urgence = tk.OptionMenu(add_window, urgence_var, "", "!", "!!", "!!!")
        dropdown_urgence.grid(row=1, column=1, sticky="w", padx=10, pady=5)

        tk.Label(add_window, text="Date :").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        day_var = tk.StringVar(add_window)
        day_var.set("01")
        dropdown_day = tk.OptionMenu(add_window, day_var, *[str(day).zfill(2) for day in range(1, 32)])
        dropdown_day.grid(row=2, column=1, sticky="w", padx=10, pady=5)

        month_var = tk.StringVar(add_window)
        month_var.set("01")
        dropdown_month = tk.OptionMenu(add_window, month_var, *[str(month).zfill(2) for month in range(1, 13)])
        dropdown_month.grid(row=2, column=1, sticky="w", padx=80, pady=5)


        year_var = tk.StringVar(add_window)
        year_var.set("2020")
        dropdown_year = tk.OptionMenu(add_window, year_var, *[str(year) for year in range(2020, 2031)])
        dropdown_year.grid(row=2, column=1, sticky="w", padx=150, pady=5)

        tk.Label(add_window, text="Heure :").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        hour_var = tk.StringVar(add_window)
        hour_var.set("00")
        dropdown_hour = tk.OptionMenu(add_window, hour_var, *[str(hour).zfill(2) for hour in range(0, 24)])
        dropdown_hour.grid(row=3, column=1, sticky="w", padx=10, pady=5)

        minute_var = tk.StringVar(add_window)
        minute_var.set("00")
        dropdown_minute = tk.OptionMenu(add_window, minute_var, *[str(minute).zfill(2) for minute in range(0, 60)])
        dropdown_minute.grid(row=3, column=1, sticky="w", padx=80, pady=5)

        btn_ajouter = tk.Button(add_window, text="Ajouter", command=lambda: self.add_task(add_window, entry_nom.get(), urgence_var.get(), f"{day_var.get()}/{month_var.get()}/" + year_var.get(), f"{hour_var.get()}h{minute_var.get()}"))
        btn_ajouter.grid(row=4, columnspan=4, pady=10)

    def show_task_details(self, event):
        # Fonction pour afficher les détails d'une tâche lors d'un double-clic
        selected_index = self.task_listbox.curselection()  # Récupérer l'index de la tâche sélectionnée
        if selected_index:
            index = selected_index[0]
            selected_task = self.tasks[index]  # Récupérer la tâche correspondante à l'index

            # Créer une nouvelle fenêtre pour afficher les détails de la tâche sélectionnée
            detail_window = tk.Toplevel(self.root)
            detail_window.title("Task Details")

            # Afficher les détails de la tâche et les boutons pour modifier ou supprimer
            tk.Label(detail_window, text="Détail de la tâche:").pack()
            entry_detail = tk.Entry(detail_window, width=50)
            entry_detail.insert(tk.END, selected_task)
            entry_detail.pack(padx=10, pady=10)

            btn_modifier = tk.Button(detail_window, text="Modifier", command=lambda: self.modify_task(detail_window, index, entry_detail.get()))
            btn_modifier.pack(side=tk.LEFT, padx=5, pady=5)
            btn_supprimer = tk.Button(detail_window, text="Supprimer", command=lambda: self.delete_task(detail_window, index))
            btn_supprimer.pack(side=tk.RIGHT, padx=5, pady=5)

    def display_menu(self):
        pass

    def add_task(self, window, name, urgency, date, time):
        # Fonction pour ajouter une tâche à la liste et fermer la fenêtre d'ajout
        if name:
            task = f"{name}"
            if urgency:
                task += f" {urgency}"
            if date != "01/01/2020":
                task += f" - {date}"
            if time != "00h00":
                task += f" - {time}"
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            window.destroy()  # Ferme la fenêtre externe
        else:
            messagebox.showwarning("Erreur", "Veuillez entrer le nom de la tâche.")

    def modify_task(self, window, index, new_task):
        # Fonction pour modifier une tâche dans la liste et fermer la fenêtre de détails
        if new_task:
            self.tasks[index] = new_task
            self.task_listbox.delete(index)
            self.task_listbox.insert(index, new_task)
            window.destroy()  # Ferme la fenêtre externe
        else:
            messagebox.showwarning("Erreur", "Veuillez entrer le nouveau nom de la tâche.")

    def delete_task(self, window, index):
        # Fonction pour supprimer une tâche de la liste et fermer la fenêtre de détails
        del self.tasks[index]
        self.task_listbox.delete(index)
        window.destroy()  # Ferme la fenêtre externe