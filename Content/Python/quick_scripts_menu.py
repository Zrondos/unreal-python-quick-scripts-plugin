"""
Module Name: quick_scripts_menu

This module defines the setup for a submenu within Unreal Engine's main menu. 
It adds a "Quick Scripts" submenu, allowing users easy access to custom scripts.

Functions
---------
create_submenu()
    Adds the "Quick Scripts" submenu to the main menu in Unreal Engine, 
    using predefined constants for menu path, label, and tooltip.
"""

import unreal
from constants import MAIN_MENU_PATH, QUICKSCRIPTS_MENU_LABEL, QUICKSCRIPTS_MENU_NAME, QUICKSCRIPTS_SECTION_NAME

def create_submenu():
    """
    Adds a "Quick Scripts" submenu to the main Unreal Engine menu. 
    This function defines and initializes the submenu with a label and tooltip 
    to guide users in accessing custom scripts.
    """
    menus = unreal.ToolMenus.get()
    main_menu = menus.find_menu(MAIN_MENU_PATH)
    main_menu.add_sub_menu(owner=QUICKSCRIPTS_MENU_NAME,
                           section_name=QUICKSCRIPTS_SECTION_NAME,
                           name=QUICKSCRIPTS_MENU_NAME,
                           label=QUICKSCRIPTS_MENU_LABEL,
                           tool_tip='See your Quick Scripts')
    menus.refresh_all_widgets()