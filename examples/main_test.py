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

# title           :main_test.py
# description     :Example for menu system.
# author          :Eric Kimsey
# usage           :python main_test.py
# notes           :
# python_version  :3.5+
# =======================================================================

try:
    from menu_system import menu_manager
    from my_menus.main_menu import MainMenu
except ImportError as error:
    print('Cannot find module, make sure to copy menu_system project into the examples directory.\n' + str(error))
    quit()

# =======================
#   PROGRAM ENTRY POINT
# =======================
# Create root of the menu system.
root_menu = MainMenu()
menu_manager.menu_logic(root_menu)
