"""
Author: Jasmine Frye
Program: Arete game
Vision: open-world MMO without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Player race classes and maps are imported from separate files
"""

import pygame, pandas
from file_paths import get_character_save_file
from graphical_menus import PyMenu
from player_character.dryad import Dryad
from player_character.fury import Fury
from player_character.naiad import Naiad
from player_character.satyr import Satyr

# LOAD & TRANSLATE CHARACTERS FROM THE CSV FILE
def load_characters():
    df = pandas.read_csv(get_character_save_file())
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

def main():
    """info = pygame.display.Info()
    desktop_width = info.current_w
    desktop_height = info.current_h"""
    desktop_height = 1080
    desktop_width = 1920
    menu = PyMenu(desktop_height, desktop_width)
    # Open the main menu
    menu.open_main_menu()
    
    # Game loop
    running = True
    while running:
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()