import pygame

# Initialize Pygame
pygame.init()

"""# Set up the game window
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Hello Pygame")

# Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False"""

# Get information about the current display to determine native resolution
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h

# Set the display mode to fullscreen using the native resolution
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

pygame.display.set_caption("Arete")

# Game loop (example)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # Press ESC to exit fullscreen
                running = False

    screen.fill((0, 0, 0)) # Fill the screen with black
    pygame.display.flip()

# Quit Pygame
pygame.quit()