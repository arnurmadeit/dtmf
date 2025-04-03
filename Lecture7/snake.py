import pygame
import sys
import random

pygame.init()

WIDTH_HEIGHT = 600_480
screen = pygame.display.set_mode(WIDTH_HEIGHT)
pygame.display.set_caption("Snake Dead")

font = pygame.font_Font(None, 30)

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

snake_pos = {100, 50}
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"
change_to = snake_direction
speed = 15

food_pos = [random.randrange]

running = True
while running: 
    for event in pygame.event_get():
        if event.type == pygame.QUIT():
            running = False
            sys.exit() 