"""
Author: Jasmine Frye
Program: Arete game
Vision: open-world MMO without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Player race classes and maps are imported from separate files
"""


import pygame
import os


# Initialize Pygame
pygame.init()

# Screen setup
height = 600
width = 1200
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Arete")

script_dir = os.path.dirname(os.path.abspath(__file__))
bg_file_name = "Graphics\Arete_BG_Clouds.png"
bg_file = os.path.join(script_dir, bg_file_name)

background_image = pygame.image.load(bg_file).convert_alpha()
background_image = pygame.transform.scale(background_image, (width, height))
screen.blit(background_image, (0, 0))

# Color constants
MIST = (243, 248, 255)
AZURE = (83, 172, 197)
COBALT = (21, 78, 114)
NAVY = (14, 41, 72)

# Menu setup


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