# Menu System
Menu system is a shell menu system implemented in Python 3. It provides a number of stock command line menus that can be inherited from to create your own menus.

## Required
* Python 3.5 or newer

## Usage
1. Copy the menu_system project folder into your Python 3 project.
2. Import the menu_system menus as needed. For example: `from menu_system.menu_types.option_select import OptionSelect`
3. Create your own menu class and inherit the menu class of the type of menu you would like to create. Create an __init__ method for your new class. In the __init__ method, call the super classes' __init__ method. You must also implement the process_input method which is executed when the user enters input. This method handles the what happens with the input (open a new menu, write data to a database, etc.). Finally, at your program entry point, create an instance of your menu and pass it to the menu_manager's menu_logic method. See examples below for more details.

## Menu Types
*Menu name:* | *Description:*
--|--
OptionSelect | Prints a list of options and special options to select from on the screen along with a title, prompt, and an optional additional message (displayed below the title).
StatusMessage | Prints a message to the screen along with a title, message, and prompt.
TextEntry | Prints a prompt for the user to enter input along with a title, special options, prompt, and optional additional message (displayed below the title).

## Examples
### main.py
```python
from menu_system import menu_manager
from my_menus.main_menu import MainMenu

# =======================
#   PROGRAM ENTRY POINT
# =======================
# Create root of the menu system.
root_menu = MainMenu()
menu_manager.menu_logic(root_menu)
```

### main_menu.py
```python
from my_menus.next_menu import NextMenu
from my_menus.another_menu import AnotherMenu
from menu_system.menu_types.option_select import OptionSelect

class MainMenu(OptionSelect):  #Inherit from OptionSelect menu
    TITLE = 'Main Menu'

    def __init__(self):
        """
        Create MainMenu object.
        """
        prompt = 'Which one? '
        options = {
            '1': NextMenu.TITLE,
            '2': AnotherMenu.TITLE
        }
        special_options = {
            'Q': 'Quit'
        }
        super().__init__(self.TITLE, prompt, options, special_options)

    def process_input(entry: str) -> tuple:
        """
        Handle all option and special option actions.
        :param str entry: User's input
        :return tuple: True = forward into next menu or False = back to previous menu (not used for root menu, obviously), next menu to display
        """
        entry = entry.upper()
        if entry == '1':
            # Create NextMenu object
            next_menu = NextMenu()
            return True, next_menu
        elif entry == '2':
            # Create AnotherMenu object
            next_menu = AnotherMenu()
            return True, next_menu
        else:
            # Quit
            quit()
```