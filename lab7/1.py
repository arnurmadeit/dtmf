import pygame
import sys
from datetime import datetime

# Init
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Mickey Mouse Clock")

mickey_body = pygame.image.load("clock.png").convert_alpha()
left_hand = pygame.image.load("sec_hand.png").convert_alpha()    # Seconds
right_hand = pygame.image.load("min_hand.png").convert_alpha()  # Minutes

center = (300, 300)

def rotate_hand(image, angle, pivot):
    rotated_image = pygame.transform.rotate(image, -angle)
    new_rect = rotated_image.get_rect(center=pivot)
    return rotated_image, new_rect

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    now = datetime.now()
    seconds = now.second
    minutes = now.minute

    second_angle = seconds * 6  # 360 / 60
    minute_angle = minutes * 6

    rotated_left, rect_left = rotate_hand(left_hand, second_angle, center)
    rotated_right, rect_right = rotate_hand(right_hand, minute_angle, center)

    screen.blit(mickey_body, (0, 0))  # Assume mickey_body is centered at (0, 0)
    screen.blit(rotated_right, rect_right)
    screen.blit(rotated_left, rect_left)

    pygame.display.flip()
    clock.tick(1)
