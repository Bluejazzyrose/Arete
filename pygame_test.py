import pygame

# Initialize Pygame
pygame.init()

# Set display mode to windowed
screen = pygame.display.set_mode((1200, 600), pygame.RESIZABLE)
screen.fill((0, 0, 0)) # Fill the screen with black

pygame.display.set_caption("Arete")

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