#!/usr/bin/python3

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
