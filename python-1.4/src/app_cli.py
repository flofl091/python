# TO DO LIST - Version 1.4


from app import ToDoListApp

class ToDoListCLI(ToDoListApp):
    def __init__(self):
        super().__init__()
        self.display_menu()

    def display_menu(self):
        while True:
            print("\n1. Ajouter une tâche")
            print("2. Afficher les détails d'une tâche")
            print("3. Modifier une tâche")
            print("4. Supprimer une tâche")
            print("5. Quitter")

            choice = input("Entrez votre choix : ")
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
                print("Choix invalide. Veuillez réessayer.")

    def add_task_cli(self):
        name = input("Nom de la tâche : ")
        urgency = input("Choisir une priorité (!, !!, !!!) : ")
        date = input("Entrez la date de la tâche (YYYY-MM-DD) : ")
        time = input("Entrez l'heure de la tâche (HH:MM) : ")
        self.add_task(name, urgency, date, time)

    def show_task_details_cli(self):
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def modify_task_cli(self):
        self.show_task_details_cli()
        index = int(input("Entrez l'index de la tâche que vous souhaitez modifier : ")) - 1
        new_task = input("Entrez la nouvelle tâche : ")
        self.modify_task(index, new_task)

    def delete_task_cli(self):
        self.show_task_details_cli()
        index = int(input("Entrez l'index de la tâche que vous souhaitez supprimer : ")) - 1
        self.delete_task(index)