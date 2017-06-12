#!/usr/bin/python

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

        # Check input against options and special_inputs
        if entry.upper() in self._options or entry.lower() in self._options:
            return True, entry
        elif entry.upper() in self._special_options or entry.lower() in self._special_options:
            return True, entry
        else:
            self.val_input = False
            return False, 'ERROR: Invalid option! '
