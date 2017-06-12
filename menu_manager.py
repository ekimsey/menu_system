#!/usr/bin/python

# title           :menu_manager.py
# description     :Manage menu system for Biblion Admin.
# author          :Eric Kimsey
# usage           :
# notes           :
# python_version  :3.5+
# =======================================================================

from collections import deque
from menu_system.menu_types import BaseMenu

menu_stack = deque()


def menu_logic(root_menu: BaseMenu) -> None:
    """
    Main menu logic loop.
    :param BaseMenu root_menu: Root menu
    :return None: Nothing
    """
    menu_stack.append(root_menu)

    while True:
        curr_menu = menu_stack[len(menu_stack) - 1]
        sel = curr_menu.menu_logic()
        # Logger.log_message(1, 'ret_val: (' + str(sel[0]) + ', ' + str(sel[1]) + ')')
        if sel[0]:
            ret_val = curr_menu.process_input(sel[1])
        else:
            # invalid input
            curr_menu.inval_prompt = sel[1]
            continue
        if ret_val[0]:
            menu_stack.append(ret_val[1])
        else:
            curr_menu.val_input = False
            curr_menu.inval_prompt = ret_val[1]


def back() -> None:
    """
    Remove last menu in the menu_stack.
    :return None: Nothing
    """
    old_menu = menu_stack.pop()
    del old_menu


def to_menu_root() -> None:
    """
    Remove all but the main menu from the menu_stack.
    :return None: Nothing
    """
    while len(menu_stack) > 1:
        old_menu = menu_stack.pop()
        del old_menu
