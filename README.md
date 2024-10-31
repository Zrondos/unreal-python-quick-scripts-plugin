# Unreal Engine Quick Scripts Plugin

This Unreal Engine plugin adds a "Quick Scripts" dropdown menu to the main menu bar. This dropdown menu allows you to quickly run Python scripts located in your projects "/Scripts/Python" directory.

<img src="./Resources/demo.gif">

## Installation
1. Download the "Content" folder and unzip it
2. Copy the unzipped folder into your Unreal Engine projects "/Plugins" folder
3. Install and enable the <a href="https://dev.epicgames.com/documentation/en-us/unreal-engine/scripting-the-editor-using-python?application_version=4.27#setupyourprojecttousepython">"Python Script Editor Plugin"</a> for your project.
4. Enable the Quick Scripts Plugin (Edit -> Plugins -> Installed -> tool)
5. Restart Unreal

## Use
1. Create a "Scripts/Python" directory if it does not already exist
2. Save Python scripts in the directory
3. Click "Quick Scripts" from the Main Menu
4. Click on the name of your script to execute it

Note:
When adding new scripts to the "/Scripts/Python" directory, click the "Refresh" button in the Quick Scripts dropdown menu to reload the contents

## Examples
Copy the files in "/Examples" to your projects "/Scripts/Python" directory to run example scripts from the Quick Scripts menu