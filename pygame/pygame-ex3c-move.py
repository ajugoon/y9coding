# Simple pygame example from https://realpython.com

# Import and initialize the pygame library
import pygame, sys
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

hero_X = 250
hero_Y = 250
colour_R = 0
colour_G = 0
colour_B = 255

while running:

    colour_R = randrange(256)
    colour_G = randrange(256)
    colour_B = randrange(256)

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit(0)

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_LEFT]:
        hero_X -= 5

    if keys_pressed[pygame.K_RIGHT]:
        hero_X += 5

    if keys_pressed[pygame.K_UP]:
        hero_Y -= 5

    if keys_pressed[pygame.K_DOWN]:
        hero_Y += 5


    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle at the location of the mouse with a random colour
    pygame.draw.circle(screen, (colour_R, colour_G, colour_B), (hero_X, hero_Y) , 25)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()