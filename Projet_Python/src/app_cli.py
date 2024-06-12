import os
import sys
from app import Applications

class Terminal(Applications):
    project_name = "Python Terminal"
    project_version = float(1.0)

    """ Constructor """ 
    def __init__(self):    
        # Instance attributes
        self.terminal_state = "LOADING"
        
        self.launch_app()

    def launch_app(self):
        self.clear_terminal()
        print(f"Welcome to the {Terminal.project_name}")

    def app_main_menu (self):
        print (f"Main menu\n 1) Start Game\n 2) Options\n 3) Quit Game")

    def option_app(self):
        print(f"Veuillez indiquer votre age / poids / taille afin de calculer votre IMC")

    def quit_app (self):
        exit()

    def clear_terminal(self):
        if(sys.platform == "win32"):
            os.system('cls')
        elif(sys.platform == 'darwin'):
            os.system('clear')
        else:
            os.system('cls')