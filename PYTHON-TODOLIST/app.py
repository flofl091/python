

from abc import ABC, abstractmethod

class ToDoListApp(ABC):
    @abstractmethod
    def display_menu(self):
        pass

    @abstractmethod
    def add_task(self, name, urgency, date, time):
        pass

    @abstractmethod
    def show_task_details(self):
        pass

    @abstractmethod
    def modify_task(self):
        pass

    @abstractmethod
    def delete_task(self):
        pass
