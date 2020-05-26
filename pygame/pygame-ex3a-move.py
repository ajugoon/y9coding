# Simple pygame example from https://realpython.com

# Import and initialize the pygame library
import pygame

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

# Create the screen object, i.e. the "drawing window"
screen = pygame.display.set_mode([500, 500])

# Set the game to "Run" until the user asks to quit
running = True

########################### THE MAIN GAME LOOP ################################

while running:

    ########################### PROCESS INPUTS ################################
    for event in pygame.event.get():
       
        if event.type == KEYDOWN:
            
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

    ###################### UPDATE THE STATE OF OBJECTS ########################  

        # obtain the location of the mouse
        hero_XY = pygame.mouse.get_pos()


    ########################### GENERATE OUTPUTS ##############################
    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle at the location of the mouse
    pygame.draw.circle(screen, (0, 0, 255), hero_XY , 75)

    # Flip the display - update the screen
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()