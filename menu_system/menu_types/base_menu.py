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

# title           :base_menu.py
# description     :BaseMenu class definition.
# author          :Eric Kimsey
# usage           :
# notes           :
# python_version  :3.5+
# =======================================================================

import os


class BaseMenu:
    inval_prompt = 'WARNING: Invalid input! '
    val_input = True

    def __init__(self, title: str, prompt: str):
        """
        Initialize menu base parameters.
        :param str title: Title to be displayed at the top of the menu
        :param str prompt: Prompt to be displayed to the user for input
        """
        self.title = title
        self._prompt = prompt

    def _print_header(self) -> None:
        """
        Clear screen and print menu header (Ludus version and menu title) to the screen.
        :return None: Nothing
        """
        self.clear_screen()
        print(self.title + '\n')

    @staticmethod
    def clear_screen() -> None:
        """
        Clear screen of any text.
        :return None: Nothing
        """
        os.system('clear')
        os.system('clear')
