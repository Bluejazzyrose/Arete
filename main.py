"""
Author: Jasmine Frye
Program: Arete game
Vision: open-world MMO without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Player race classes and maps are imported from separate files
"""

import pygame
from graphical_menus import PyMenu

def main():
    menu = PyMenu()
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