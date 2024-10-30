"""
Module Name: refresh_section

This module defines the functionality to create and manage the "Refresh" 
section within the Unreal Engine Quick Scripts menu. It includes a class 
for the menu entry that refreshes the "Your Scripts" section and a 
function to set up the "Refresh" section within the menu.

Classes
-------
RefreshSectionEntry:
    A clickable menu entry for refreshing the "Your Scripts" section

Functions
---------
add_refresh_section()
    Creates, adds, and populates the 'RefreshSection' of the Quick Scripts Menu.
"""

import unreal
import scripts_section
from constants import QUICKSCRIPTS_MENU_NAME, QUICKSCRIPTS_MENU_PATH, REFRESH_SECTION_NAME, REFRESH_SECTION_LABEL, REFRESH_ENTRY_NAME


@unreal.uclass()
class RefreshSectionEntry(unreal.ToolMenuEntryScript):
    """
    A custom menu entry class that creates an entry for the "Refresh" section of the Quick Scripts menu.
    Subclass of 'unreal.ToolMenuEntryScript"

    Methods
    -------
    execute(self,context)
        Refreshes the "Your Scripts" section 
    """

    def __init__(self):
        """
        Initializes a new instance of the RefreshSectionEntry class. 
        """

        super().__init__()
        self.init_entry(
            owner_name=QUICKSCRIPTS_MENU_NAME,
            menu=QUICKSCRIPTS_MENU_PATH,
            section=REFRESH_SECTION_NAME,
            name=REFRESH_ENTRY_NAME,
            label=REFRESH_SECTION_LABEL,
            tool_tip=f"Click to refresh scripts."
        )
        self.get_editor_property("data").set_editor_property(
            "insert_position",
            unreal.ToolMenuInsert(position=unreal.ToolMenuInsertType.FIRST))

    @unreal.ufunction(override=True)
    def execute(self, context):
        """
        Refreshes the list of entries of the "Your Scripts" section on-click.

        Parameters
        ----------
        context : unreal.ToolMenuContext
            Provides contextual information from UE Editor when the menu entry is triggered.
        """

        scripts_section.create_scripts_section(refresh=True)


def add_refresh_section():
    """
    Adds a section named "RefreshSection" the Quick Scripts menu.
    Creates and adds a RefreshSectionEntry instance to the Refresh Section
    """

    menus = unreal.ToolMenus.get()
    custom_menu = menus.find_menu(QUICKSCRIPTS_MENU_PATH)
    custom_menu.add_section(
        section_name=REFRESH_SECTION_NAME,
        label=REFRESH_SECTION_LABEL
    )

    refresh_entry = RefreshSectionEntry()
    custom_menu.add_menu_entry_object(refresh_entry)

    menus.refresh_menu_widget(QUICKSCRIPTS_MENU_PATH)
