#!/usr/bin/python

# title           :text_entry.py
# description     :TextEntry class definition.
# author          :Eric Kimsey
# usage           :
# notes           :
# python_version  :3.5+
# =======================================================================
from menu_system.menu_types import BaseMenu


class TextEntry(BaseMenu):

    def __init__(self, title: str, prompt: str,
                 special_options: dict, add_message: str = None):
        """
        Create Text_Entry menu.
        :param str title: Title to be displayed at the top of the menu
        :param str prompt: Prompt to be displayed to the user for input
        :param dict special_options: Special options from which the user may choose
        :param str add_message: Additional message to be displayed to the user
        """
        super().__init__(title, prompt)
        self._special_options = special_options
        self._add_message = add_message
        self.val_input = True

    def _display(self) -> None:
        """
        Display text entry menu.
        :return None: Nothing
        """
        # Header
        self._print_header()
        # Optional selection
        if self._add_message is not None:
            print(self._add_message + '\n')
        # Special options
        for key in sorted(self._special_options.keys()):
            print('[' + key + ']\t' + self._special_options[key])
        print()

    def menu_logic(self) -> tuple:
        """
        Display menu, get input, return input.
        :return tuple: True = Success or False = Fail, user input or status message
        """
        self._display()
        if self.val_input:
            # If last input was valid or this is first prompt, use regular prompt
            entry = input(self._prompt)
        else:
            # Else, last input was invalid, clear screen and print invalid input error before prompt
            entry = input(self.inval_prompt + self._prompt)
            self.val_input = True

        if len(entry) < 1:
            return False, 'Nothing entered! '
        else:
            return True, entry
