#!/usr/bin/python3

from menu_system import menu_manager
from menu_system.menu_types.text_entry import TextEntry
from menu_system.menu_types.status_message import StatusMessage

class AnotherMenu(TextEntry):
    TITLE = 'Another Menu'

    def __init__(self):
        """
        Create AnotherMenu.
        """
        prompt = 'Enter some text: '
        special_options = {
            'B': 'Back',
            'M': 'Main Menu',
            'Q': 'Exit'
        }
        add_message = 'This menu allows you to take longer strings of user input.'
        super().__init__(self.TITLE, prompt, special_options, add_message)

    @staticmethod
    def process_input(entry: str) -> tuple:
        """
        Handle all option and special option actions.
        :param str entry: User's input
        :return tuple: True = Success or False = Fail, next menu or status message
        """
        if entry.upper() == 'B':
            # Call the menu manager function to go back to the previous menu
            menu_manager.back()
            return False, ''
        elif entry.upper() == 'M':
            # Call the menu manager function to go back to the root (main) menu
            menu_manager.to_menu_root()
            return False, ''
        elif entry.upper() == 'Q':
            # Quit
            quit()
        else:
            # Input is good
            status = StatusMessage('Status Message', 'Press any key to return to the last menu', 'You entered: ' + entry)
            status.menu_logic()
            return False, ''
