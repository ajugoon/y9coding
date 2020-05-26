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

enemy_X = randrange(500) #enemy can appear anywhere along the x-axis 
enemy_Y = 10 #remember the y-axis is inverted so this very near the "top"
enemy_Speed = randrange(5, 10) # the enemy will descend at a random speed (in pixels)

hero = pygame.Rect(hero_X, hero_Y, 10, 10) # this will be the bounding box of the hero
enemy = pygame.Rect(enemy_X, enemy_Y, 10, 10) # this will be the bounding box of the enemy

hit = False # Initially there are no hits

while running:

    ##############################################################################
    # Step 1 of the Main Game Loop: 
    # Look for any form of keyboard or mouse input

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
    
    ##############################################################################
    # Step 2 of the Main Game Loop: 
    # Update any positional coordinates concerned with the enemy or hero
    # This includes the speed being added to the y-coordinate to simulate "falling"

    if enemy_Y > 500: # if enemy "falls off" the bottom of the window
        enemy_X = randrange(500) # enemy can appear anywhere along the x-axis 
        enemy_Y = 10 # reset the value of the enemy's y-coordinate


    enemy_Y = enemy_Y + enemy_Speed

    if (enemy.colliderect(hero) and hit == False):
        hit = True
        print("hit!")

    ##############################################################################
    # Step 3 of the Main Game Loop:
    # Draw all of the objects onto the screen with the most up-to-date coordinates

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Update the Hero and Enemy Bounding Boxes
    hero = pygame.Rect(hero_X, hero_Y, 20, 20) # this will be the bounding box of the hero
    enemy = pygame.Rect(enemy_X, enemy_Y, 20, 20) # this will be the bounding box of the enemy

    # Draw a solid blue circle at the location of the mouse with a random colour
    pygame.draw.circle(screen, (255, 0, 0), (hero_X, hero_Y), 20) # draw the hero
    pygame.draw.rect(screen, (0, 0, 255), (enemy_X, enemy_Y, 10, 10)) # draw the enemy

    # Flip the display - update the screen
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
