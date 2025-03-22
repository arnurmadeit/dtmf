import pygame
import sys


pygame.init()
screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("🔴 Move the Ball")


WHITE = (255, 255, 255)
RED = (255, 0, 0)

radius = 25
x, y = screen_width // 2, screen_height // 2
step = 20  

clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)  

    pygame.draw.circle(screen, RED, (x, y), radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y - radius - step >= 0:
                y -= step
            elif event.key == pygame.K_DOWN and y + radius + step <= screen_height:
                y += step
            elif event.key == pygame.K_LEFT and x - radius - step >= 0:
                x -= step
            elif event.key == pygame.K_RIGHT and x + radius + step <= screen_width:
                x += step

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
