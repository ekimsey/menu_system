#!/usr/bin/python3

"""
Menu System is a shell interface menu manager.
Copyright (C) 2018  Eric Kimsey

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# title           :another_menu.py
# description     :Example menu for menu system.
# author          :Eric Kimsey
# usage           :
# notes           :
# python_version  :3.5+
# =======================================================================

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
