

from app_cli import ToDoListCLI  # Importer la classe ToDoListCLI depuis le fichier app_cli.py
from app_gui import ToDoListGUI  # Importer la classe ToDoListGUI depuis le fichier app_gui.py

def main(application_mode: str = "Terminal"):
    if application_mode == "Terminal":
        print("Starting in CLI mode")  # Afficher un message pour indiquer que le programme démarre en mode CLI
        todo_app = ToDoListCLI()  # Créer une instance de ToDoListCLI pour démarrer l'application en mode CLI
    elif application_mode == "GUI":
        print("Starting in GUI mode")  # Afficher un message pour indiquer que le programme démarre en mode GUI
        todo_app = ToDoListGUI()  # Créer une instance de ToDoListGUI pour démarrer l'application en mode GUI
    else:
        print("This command is unavailable")  # Afficher un message si le mode spécifié n'est pas disponible

# Main guard
if __name__ == "__main__":
    main("GUI")  # Appeler la fonction main() avec le mode GUI comme argument lors de l'exécution directe du script