#!/usr/bin/python

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
