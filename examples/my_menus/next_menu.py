#!/usr/bin/python3

from menu_system import menu_manager
from my_menus.another_menu import AnotherMenu
from menu_system.menu_types.option_select import OptionSelect
from menu_system.menu_types.status_message import StatusMessage

class NextMenu(OptionSelect):  #Inherit from OptionSelect menu
    TITLE = 'Next Menu'

    def __init__(self):
        """
        Create NextMenu object.
        """
        prompt = 'Pick one: '
        options = {
            '1': 'Dead End',
            '2': AnotherMenu.TITLE
        }
        special_options = {
            'B': 'Back',
            'M': 'Main Menu',
            'Q': 'Quit'
        }
        super().__init__(self.TITLE, prompt, options, special_options)

    @staticmethod
    def process_input(entry: str) -> tuple:
        """
        Handle all option and special option actions.
        :param str entry: User's input
        :return tuple: True = forward into next menu or False = back to previous menu, next menu to display
        """
        entry = entry.upper()
        if entry == '1':
            # Create StatusMessage object
            status = StatusMessage('Dead End', 'Press any key to return to the last menu', 'This is a StatusMessage')
            status.menu_logic()
            ''' Do something else here if you don't want to return to this menu '''
            return False, ''
        elif entry == '2':
            # Create AnotherMenu object
            another_menu = AnotherMenu()
            return True, another_menu
        if entry.upper() == 'B':
            # Call the menu manager function to go back to the previous menu
            menu_manager.back()
            return False, ''
        elif entry.upper() == 'M':
            # Call the menu manager function to go back to the root (main) menu
            menu_manager.to_menu_root()
            return False, ''
        else:
            # Quit
            quit()