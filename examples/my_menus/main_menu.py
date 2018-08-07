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

# title           :main_menu.py
# description     :Example menu for menu system.
# author          :Eric Kimsey
# usage           :
# notes           :
# python_version  :3.5+
# =======================================================================

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

    @staticmethod
    def process_input(entry: str) -> tuple:
        """
        Handle all option and special option actions.
        :param str entry: User's input
        :return tuple: True = forward into next menu or False = back to previous menu (not used for root menu, obviously), next menu to display
        """
        if entry == '1':
            # Create NextMenu object
            next_menu = NextMenu()
            return True, next_menu
        elif entry == '2':
            # Create AnotherMenu object
            another_menu = AnotherMenu()
            return True, another_menu
        else:
            # Quit
            quit()
