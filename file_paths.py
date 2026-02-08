"""
Author: Jasmine Frye
Program: Arete game
Vision: open-world MMO without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Player race classes and maps are imported from separate files
"""

import os

# Create a file path to the parent directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def get_maps_file():
    # Create a file path to the maps file
    file_name = "maps/maps.json"
    file_route = os.path.join(SCRIPT_DIR, file_name)
    return file_route

def get_character_save_file():
    # Create a file path to the characters save file
    file_name = "characters.csv"
    file_route = os.path.join(SCRIPT_DIR, file_name)
    return file_route

def get_menu_bg_file():
    # Create a file path to the menu bg graphic
    file_name = "Graphics\\Arete_BG_Clouds.png"
    file_route = os.path.join(SCRIPT_DIR, file_name)
    return file_route