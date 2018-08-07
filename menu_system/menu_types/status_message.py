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

# title           :status_message.py
# description     :StatusMessage class definition.
# author          :Eric Kimsey
# usage           :
# notes           :
# python_version  :3.5+
# =======================================================================

from menu_system.menu_types.base_menu import BaseMenu


class StatusMessage(BaseMenu):

    def __init__(self, title: str, prompt: str, message: str):
        """
        Create Status_Message menu.
        :param str title: Title to be displayed at the top of the menu
        :param str prompt: Prompt to be displayed to the user for input
        :param str message: Status to be displayed to the user
        """
        super().__init__(title, prompt)
        self._message = message

    def _display(self) -> None:
        """
        Display status message.
        :return None: Nothing
        """
        self._print_header()
        print(self._message + '\n')

    def menu_logic(self) -> None:
        """
        Display status message, take user input to advance to next menu.
        :return None: Nothing
        """
        self._display()
        input(self._prompt)
