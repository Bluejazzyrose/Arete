"""
Author: Jasmine Frye
Program: Arete game
Vision: open-world MMO without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Player race classes and maps are imported from separate files
"""


import pygame
import pygame_menu as pm
from pygame_menu.themes import Theme
from pygame_menu.baseimage import BaseImage, IMAGE_MODE_FILL
import os
import pandas

from player_character.dryad import Dryad
from player_character.fury import Fury
from player_character.naiad import Naiad
from player_character.satyr import Satyr


# Initialize Pygame
pygame.init()
# Screen setup
HEIGHT = 1080
WIDTH = 1920
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arete")

# CREATE FILE PATHS
# Create a file path to the parent directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Create a file path to the menu bg graphic
menu_bg_file_name = "Graphics\\Arete_BG_Clouds.png"
menu_bg_file_path = os.path.join(SCRIPT_DIR, menu_bg_file_name)
# Create a file path to the characters save file
csv_file_name = "characters.csv"
character_save_file = os.path.join(SCRIPT_DIR, csv_file_name)
# Convert the csv file into a pandas dataframe
characters = pandas.read_csv(character_save_file)
char_selectables = []
for index, c in characters.iterrows():
        char_selectables.append((c["name"], c["race"]))

# Color constants
MIST = (243, 248, 255)
AZURE = (83, 172, 197)
COBALT = (21, 78, 114)
NAVY = (14, 41, 72)


# LOAD & TRANSLATE CHARACTERS FROM THE CSV FILE
def load_characters():
    df = pandas.read_csv(character_save_file)
    characters = []
    for index, c in df.iterrows():           
        if c['race'] == 'dryad':
            character = Dryad(c['name'])
        elif c['race'] == 'satyr':
            character = Satyr(c['name'])
        elif c['race'] == 'fury':
            character = Fury(c['name'])
        elif c['race'] == 'naiad':
            character = Naiad(c['name'])
        character.x = c['x']
        character.y = c['y']
        character.hp = c['hp']
        characters.append(character)
    return characters


# THEME SETUP
def menu_bg_theme():
    menu_theme = Theme()
    # Menu bg graphic - clouds
    menu_theme.background_color = BaseImage(image_path=menu_bg_file_path, drawing_mode=IMAGE_MODE_FILL)
    # Button colors & margin
    menu_theme.widget_background_color = NAVY
    menu_theme.widget_font_color = MIST
    menu_theme.widget_background_inflate = (10, 10)
    menu_theme.widget_margin = (0, 50)
    return menu_theme


# CHARACTER SELECTION MENU SETUP
def open_charselect():
    character_select = pm.Menu(title = "Character Selection Menu",
                               width = WIDTH, height = HEIGHT, theme = menu_bg_theme(),
                               overflow = (True, False))
    # Play button. If clicked, opens the game
    character_select.add.button(title="Play")
    # Character select bar
    character_select.add.selector(title = "Character selected: ", items = char_selectables)
    character_select.add.button(title="Back to Main Menu", action = open_main_menu)
    # Display the menu
    character_select.mainloop(screen)


# MAIN MENU SETUP
def open_main_menu():
    menu = pm.Menu(title = "Main Menu", width = WIDTH, height = HEIGHT, theme = menu_bg_theme())
    # Character selection button. If clicked, it takes to the character selection menu
    menu.add.button(title = "Character Selection", action = open_charselect)
    # Exit Button. If clicked, it closes the window
    menu.add.button(title="Exit", action=pm.events.EXIT)
    # Display the menu
    menu.mainloop(screen)

def main():
    # Open the main menu
    open_main_menu()
    
    # Game loop
    running = True
    while running:
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()