"""
Module Name: path_manager

This module provides utility functions to interact with the 'Scripts/Python' directory.

Functions
---------
check_dir_exists() -> bool
    Returns 'True' if the 'Scripts/Python' directory exists in the Unreal Engine project.
get_scripts() -> list[str]
    Returns a list of Python script filenames located in the 'Scripts/Python' directory of the Unreal Engine project.
"""

import unreal
import os
from constants import SCRIPTS_DIR_PATH

def check_dir_exists() -> bool:
    """
    Looks for the 'Scripts/Python' directory inside the current project. Returns a 'True' if the directory exists
    """
    project_dir = unreal.Paths.project_dir()
    scripts_dir = os.path.join(project_dir, SCRIPTS_DIR_PATH)
    return os.path.isdir(scripts_dir)

def get_scripts() -> list[str]:
    """
    Returns a list of .py filenames from the 'Scripts/Python' directory
    """
    project_dir = unreal.Paths.project_dir()
    scripts_dir = os.path.join(project_dir, SCRIPTS_DIR_PATH)
    files = os.listdir(scripts_dir)
    files = [f for f in files if f.endswith(
        ".py") and os.path.isfile(os.path.join(scripts_dir, f))]
    return files