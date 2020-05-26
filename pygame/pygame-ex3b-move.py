# Simple pygame example from https://realpython.com

# Import and initialize the pygame library
import pygame
from random import random
from random import randrange

# Import pygame.locals for easier access to key coordinates

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Initialize Pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True

while running:

    
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
        
        # grab the mouse location
        hero_XY = pygame.mouse.get_pos()

        colour_R = randrange(256)
        colour_G = randrange(256)
        colour_B = randrange(256)


    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle at the location of the mouse with a random colour
    pygame.draw.circle(screen, (colour_R, colour_G, colour_B), hero_XY , 25)

    # Flip the display - update the screen
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()