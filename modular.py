from blessed import Terminal
from abc import ABC, abstractmethod

# Initialize the terminal
term = Terminal()

# Abstract base class for menus
class Menu(ABC):
    def __init__(self, manager):
        self.manager = manager  # Reference to the AppManager

    @abstractmethod
    def update(self):
        pass

# MainMenu class
class MainMenu(Menu):
    def update(self):
        print(term.clear)
        print(term.bold("Main Menu"))
        print("1. Go to Settings")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            self.manager.transition(SettingsMenu)  # Transition to SettingsMenu
        elif choice == "2":
            self.manager.transition(None)  # Exit the app
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

# SettingsMenu class
class SettingsMenu(Menu):
    def update(self):
        print(term.clear)
        print(term.bold("Settings Menu"))
        print("1. Go back to Main Menu")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            self.manager.transition(MainMenu)  # Transition to MainMenu
        elif choice == "2":
            self.manager.transition(None)  # Exit the app
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

# Manager class
class AppManager:
    def __init__(self):
        self.current_state = MainMenu(self)  # Start with the MainMenu

    def transition(self, next_state):
        """Transition to the next state."""
        if next_state is None:
            self.current_state = None  # Exit the app
        else:
            self.current_state = next_state(self)

    def run(self):
        """Run the application."""
        while self.current_state:
            self.current_state.update()
        print("Exiting...")

# Run the app
if __name__ == "__main__":
    app = AppManager()
    app.run()
