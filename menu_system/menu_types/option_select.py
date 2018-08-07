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

# title           :option_select.py
# description     :OptionSelect class definition.
# author          :Eric Kimsey
# usage           :
# notes           :
# python_version  :3.5+
# =======================================================================

from menu_system.menu_types.base_menu import BaseMenu


class OptionSelect(BaseMenu):

    def __init__(self, title: str, prompt: str,
                 options: dict, special_options: dict, add_message: str = None):
        """
        Create Option_Select menu.
        :param str title: Title to be displayed at the top of the menu
        :param str prompt: Prompt to be displayed to the user for input
        :param dict options: Options from which the user may choose
        :param dict special_options: Special options from which the user may choose
        :param str add_message: Additional message to be displayed to the user
        """
        super().__init__(title, prompt)
        self._options = options
        self._special_options = special_options
        self._add_message = add_message

    def _display(self) -> None:
        """
        Display Option_Select menu.
        :return None: Nothing
        """
        # Header
        self._print_header()
        # Optional selection
        if self._add_message is not None:
            print(self._add_message + '\n')
        # Options
        for key in sorted(self._options.keys()):
            print('[' + str(key) + ']\t' + self._options[key])
        print()
        # Special options
        for key in self._special_options.keys():
            print('[' + key + ']\t' + self._special_options[key])
        print()

    def menu_logic(self) -> tuple:
        """
        Display menu, get input, and check input against options.
        :return tuple: True = Success or False = Fail, user input or status message
        """
        # Get input from user
        self._display()
        if self.val_input:
            # If last input was valid or this is first prompt, use regular prompt
            entry = input(self._prompt)
        else:
            # Else, last input was invalid, clear screen and print invalid input error before prompt
            entry = input(self.inval_prompt + self._prompt)
            self.val_input = True

		# Scrub entry of arrow key escape characters
        entry = entry.replace('\x1b[A', '').replace('\x1b[B', '').replace('\x1b[C', '').replace('\x1b[D', '')

        # Check input against options and special_inputs
        if entry.upper() in self._options or entry.lower() in self._options:
            return True, entry
        elif entry.upper() in self._special_options or entry.lower() in self._special_options:
            return True, entry
        else:
            self.val_input = False
            return False, 'ERROR: Invalid option! '
