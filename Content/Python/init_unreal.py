"""
This is the entry-point for the plugin when the Unreal Engine Editor first starts.
It sets up the Quick Scripts Menu, then adds and populates the "Refresh" section and "Your Scripts" section.

Functions
---------
main()
    quick_scripts_menu.create_submenu(): 
        Creates the "LevelEditor.MainMenu.QuickScripts" submenu
    refresh_section.add_refresh_section():
        Adds the "Refresh" section "LevelEditor.MainMenu.QuickScripts" and adds "RefreshEntry" to the "Refresh" section
    scripts_section.create_scripts_section(refresh=False)
        Creates the "YourScripts" section and populates the section with an entry for each .py file in "/Scripts/Python".
        'refresh' is set to 'False', indicating that the scripts section is not triggered by clicking "RefreshEntry"
"""

import unreal
import refresh_section
import quick_scripts_menu
import scripts_section


def main():
    unreal.log("Setting up Quick Scripts Plugin")
    quick_scripts_menu.create_submenu()
    refresh_section.add_refresh_section()
    scripts_section.create_scripts_section(refresh=False)
    menus = unreal.ToolMenus.get()
    menus.refresh_all_widgets()
    unreal.log("Quick Script Plugin Setup Complete")


if __name__ == "__main__":
    main()
