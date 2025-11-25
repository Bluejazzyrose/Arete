"""
Author: Jasmine Frye
Program: Arete game
Vision: open-world MMO without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Player race classes and maps are imported from separate files
"""


import pygame, pandas
import pygame_menu as pm
from pygame_menu.themes import Theme
from pygame_menu.baseimage import BaseImage, IMAGE_MODE_FILL
from file_paths import get_character_save_file, get_menu_bg_file

# Color constants
MIST = (243, 248, 255)
AZURE = (83, 172, 197)
COBALT = (21, 78, 114)
NAVY = (14, 41, 72)

# THEME SETUP
MENU_THEME = Theme()
# Menu bg graphic - clouds
MENU_THEME.background_color = BaseImage(image_path = get_menu_bg_file(),
                                        drawing_mode = IMAGE_MODE_FILL)
# Button colors & margin
MENU_THEME.widget_background_color = NAVY
MENU_THEME.widget_font_color = MIST
MENU_THEME.widget_background_inflate = (10, 10)
MENU_THEME.widget_margin = (0, 50)

characters = pandas.read_csv(get_character_save_file())
char_selectables = []
for index, c in characters.iterrows():
        char_selectables.append((c["name"], c["race"]))

# Pygame Menu class
class PyMenu:
    def __init__(self, height, width):
        # Initialize Pygame
        pygame.init()
        # Screen size setup
        self.HEIGHT = height
        self.WIDTH = width
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Arete")

    # CHARACTER SELECTION MENU SETUP
    def open_charselect(self):
        character_select = pm.Menu(title = "Character Selection Menu",
                                   width = self.WIDTH,
                                   height = self.HEIGHT,
                                   theme = MENU_THEME)
        # Play button. If clicked, opens the game
        character_select.add.button(title="Play")
        # Character select bar
        character_select.add.selector(title = "Character selected: ", items = char_selectables)
        character_select.add.button(title="Back to Main Menu", action = self.open_main_menu)
        # Display the menu
        character_select.mainloop(self.screen)

    # MAIN MENU SETUP
    def open_main_menu(self):
        menu = pm.Menu(title = "Main Menu",
                       width = self.WIDTH,
                       height = self.HEIGHT,
                       theme = MENU_THEME)
        # Character selection button. If clicked, it takes to the character selection menu
        menu.add.button(title = "Character Selection", action = self.open_charselect)
        # Exit Button. If clicked, it closes the window
        menu.add.button(title="Exit", action=pm.events.EXIT)
        # Display the menu
        menu.mainloop(self.screen)