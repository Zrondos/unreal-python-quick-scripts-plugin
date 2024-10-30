"""
Module Name: scripts_section

This module manages the "Your Scripts" section in Unreal Engine's Quick Scripts menu. It includes functionalities for 
creating, populating, and updating menu entries representing available Python scripts, allowing users to execute them directly from the menu.

Classes
-------
YourScriptsSectionEntry
    A clickable menu entry for executing a Python script.

Functions
---------
create_scripts_section(refresh=False)
    Creates or refreshes the 'YourScripts' section of the Quick Scripts Menu.

populate_your_scripts_section()
    Populates the section with entries for available scripts, handling cases for empty or missing directories.

add_your_scripts_entry(file_name: str)
    Adds a single script entry to the "Your Scripts" section.
"""

import unreal
import os
import path_manager
import warnings_section
from constants import SCRIPTS_DIR_PATH, QUICKSCRIPTS_MENU_PATH, QUICKSCRIPTS_MENU_NAME, YOUR_SCRIPTS_SECTION_NAME, YOUR_SCRIPTS_SECTION_LABEL


@unreal.uclass()
class YourScriptsSectionEntry(unreal.ToolMenuEntryScript):
    """
    A custom menu entry class that creates a 'Your Scripts' entry for the "Your Scripts" section of the Quick Scripts menu.
    Subclass of 'unreal.ToolMenuEntryScript'.

    Methods
    -------
    execute(context)
        Executes the associated script or handles cases where the script file is missing.

    handle_bad_entry(self, script_name: str)
        Logs a warning and refreshes the menu if the script file is not found.
    """

    def __init__(self, file_name: str):
        """
        Initializes a new instance of the YourScriptsSectionEntry class. 

        Parameters
        ----------
        file_name: str
            The name of the Python script associated with the entry
        """

        super().__init__()

        self.init_entry(
            owner_name=QUICKSCRIPTS_MENU_NAME,
            menu=QUICKSCRIPTS_MENU_PATH,
            section=YOUR_SCRIPTS_SECTION_NAME,
            name=file_name,
            label=file_name,
            tool_tip=f"Click to execute {file_name}"
        )

    @unreal.ufunction(override=True)
    def execute(self, context):
        """
        Runs the python script associated with the entry if it exists.
        If it does not exist, refreshes the section to remove the missing entry.

        Parameters
        ----------
        context : unreal.ToolMenuContext
            Provides contextual information from UE Editor when the menu entry is triggered.
        """

        project_dir = unreal.Paths.project_dir()
        scripts_dir = os.path.join(project_dir, SCRIPTS_DIR_PATH)
        script_name = self.get_editor_property(
            "data").get_editor_property("name")
        script_path = os.path.join(scripts_dir, str(script_name))
        if not os.path.exists(script_path):
            self.handle_bad_entry(script_name)
        else:
            with open(script_path, 'r') as file:
                exec(file.read())

    def handle_bad_entry(self, script_name: str):
        """
        Handles missing script files by logging a warning and refreshing the "Your Scripts" section.

        Parameters
        ----------
        script_name: str
            The name of the script associated with the entry
        """
        unreal.log(
            f"{script_name} not found. Refreshing \"Your Scripts\" menu.")
        create_scripts_section(refresh=True)


def create_scripts_section(refresh=False):
    """
    Creates or refreshes the "Your Scripts" section in the Quick Scripts menu.

    Parameters
    ----------
    refresh: bool
        Indicates if the section is being created for the first time (refresh=False) or if the section is being refreshed (refresh=True)
    """

    menus = unreal.ToolMenus.get()
    if refresh:
        menus.remove_section(QUICKSCRIPTS_MENU_PATH, YOUR_SCRIPTS_SECTION_NAME)
    custom_menu = menus.find_menu(QUICKSCRIPTS_MENU_PATH)
    custom_menu.add_section(
        section_name=YOUR_SCRIPTS_SECTION_NAME, label=YOUR_SCRIPTS_SECTION_LABEL)
    populate_your_scripts_section()


def populate_your_scripts_section():
    """
    Populates "Your Scripts" section with entries for each available Python script in the specified directory.
    Handles cases if the directory does not exist or does not contain any scripts
    """

    dir_exists = path_manager.check_dir_exists()
    if not dir_exists:
        warnings_section.handle_no_dir()
        return

    file_names = path_manager.get_scripts()
    if not file_names:
        warnings_section.handle_empty_dir()
        return

    for file_name in file_names:
        add_your_scripts_entry(file_name)

    menus = unreal.ToolMenus.get()
    menus.refresh_menu_widget(QUICKSCRIPTS_MENU_PATH)


def add_your_scripts_entry(file_name: str):
    """
    Adds a menu entry for a specified script file in the "Your Scripts" section.

    Parameters
    ----------
    file_name: str
        The file name associataed with the entry
    """

    menus = unreal.ToolMenus.get()
    custom_menu = menus.find_menu(QUICKSCRIPTS_MENU_PATH)

    your_scripts_entry = YourScriptsSectionEntry(file_name)
    custom_menu.add_menu_entry_object(your_scripts_entry)
    menus.refresh_menu_widget(QUICKSCRIPTS_MENU_PATH)
