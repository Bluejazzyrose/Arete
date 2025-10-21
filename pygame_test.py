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


# Initialize Pygame
pygame.init()

# Screen setup
HEIGHT = 600
WIDTH = 1200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arete")

script_dir = os.path.dirname(os.path.abspath(__file__))
bg_file_name = "Graphics\Arete_BG_Clouds.png"
bg_file_path = os.path.join(script_dir, bg_file_name)

background_image = pygame.image.load(bg_file_path).convert_alpha()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
screen.blit(background_image, (0, 0))

# Color constants
MIST = (243, 248, 255)
AZURE = (83, 172, 197)
COBALT = (21, 78, 114)
NAVY = (14, 41, 72)

# Menu theme setup
menu_bg = Theme()
menu_bg.background_color = BaseImage(image_path = bg_file_path,
                                     drawing_mode = IMAGE_MODE_FILL)

# Menu setup
menu = pm.Menu(title = "Main Menu",
               width = WIDTH,
               height = HEIGHT,
               theme = menu_bg)

# Settings button. If clicked, it takes to the settings menu
menu.add.button(title="Play",
                font_color=MIST,
                background_color=NAVY,
                background_inflate = (10, 10))

# Dummy label to add some spacing between the settings button and exit button
menu.add.label(title="")

# Exit Button. If clicked, it closes the window
menu.add.button(title="Exit", action=pm.events.EXIT,
                font_color=MIST,
                background_color=NAVY,
                background_inflate = (10, 10))

menu.mainloop(screen)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # Press ESC to exit fullscreen
                running = False

    pygame.display.flip()

# Quit Pygame
pygame.quit()