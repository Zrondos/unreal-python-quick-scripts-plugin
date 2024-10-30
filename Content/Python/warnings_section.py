"""
Module Name: warnings_section

Handles warning entries within the "Your Scripts" section of the Unreal Engine Quick Scripts menu. This module provides 
messages to notify users when the scripts directory is empty or missing, guiding them on how to proceed.

Classes
-------
YourScriptsWarningEntry
    Represents a non-clickable warning entry with a message to the user about issues related to the scripts directory.

Functions
---------
handle_empty_dir()
    Displays a warning entry indicating that no scripts were found in the specified directory.

handle_no_dir()
    Displays a warning entry indicating that the scripts directory is missing.
"""

import unreal
from constants import QUICKSCRIPTS_MENU_PATH, QUICKSCRIPTS_MENU_NAME, YOUR_SCRIPTS_SECTION_NAME, SCRIPTS_DIR_PATH


@unreal.uclass()
class YourScriptsWarningEntry(unreal.ToolMenuEntryScript):
    """
    A menu entry for displaying a warning in the "Your Scripts" section when there is an issue with the scripts directory.
    Subclass of 'unreal.ToolMenuEntryScript".

    Attributes
    ----------
    warning_data : dict
        Contains labels, names, and tooltips for different warning types, such as "Empty_dir" and "No_dir".

    Methods
    -------
    can_execute(context)
        Disables execution for warning entries, making them non-clickable.
    """

    warning_data = {
        "empty_dir": {"label": "No Scripts Found",
                      "name": "No Files",
                      "tool_tip": f"Please add Python scripts to \"{SCRIPTS_DIR_PATH}\" then click \"Refresh Scripts\""},
        "no_dir": {"label": f"\"{SCRIPTS_DIR_PATH}\" directory not found.",
                   "name": "No Directory",
                   "tool_tip": f"Create the \"{SCRIPTS_DIR_PATH}\" directory then click \"Refresh Scripts\""
                   }
    }

    def __init__(self, warning_type: str):
        """
        Initializes a warning entry with a specific type of warning message.

        Parameters
        ----------
        warning_type : str
            The type of warning message to display, either "empty_dir" or "no_dir".
        """

        super().__init__()
        self.init_entry(owner_name=QUICKSCRIPTS_MENU_NAME,
                        menu=QUICKSCRIPTS_MENU_PATH,
                        section=YOUR_SCRIPTS_SECTION_NAME,
                        name=self.warning_data[warning_type]['name'],
                        label=self.warning_data[warning_type]['label'],
                        tool_tip=self.warning_data[warning_type]['tool_tip'])

    @unreal.ufunction(override=True)
    def can_execute(self, context):
        """
        Prevents execution of the warning entry, making it non-interactive.

        Parameters
        ----------
        context : unreal.ToolMenuContext
            Provides context from Unreal Engine's editor.
        """

        return False


def handle_empty_dir():
    """
    Adds a warning entry to the menu when no script files are found in the specified directory.
    """
    
    menus = unreal.ToolMenus.get()
    custom_menu = menus.find_menu(QUICKSCRIPTS_MENU_PATH)

    empty_dir_entry = YourScriptsWarningEntry("empty_dir")
    custom_menu.add_menu_entry_object(empty_dir_entry)

    menus.refresh_menu_widget(QUICKSCRIPTS_MENU_PATH)


def handle_no_dir():
    """
    Adds a warning entry to the menu when the specified directory does not exist.
    """
    menus = unreal.ToolMenus.get()
    custom_menu = menus.find_menu(QUICKSCRIPTS_MENU_PATH)

    no_dir_entry = YourScriptsWarningEntry("no_dir")
    custom_menu.add_menu_entry_object(no_dir_entry)

    menus.refresh_menu_widget(QUICKSCRIPTS_MENU_PATH)
