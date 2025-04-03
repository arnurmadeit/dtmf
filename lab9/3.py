import pygame
import math

def draw_palette(screen, y, width, height):
    for x in range(width):
        color = get_color_from_palette(x, width)
        pygame.draw.rect(screen, color, (x, y, 1, height))

#the gradient bar on the top of the screen
def get_color_from_palette(x, width):
    ratio = x / width
    r = int(max(0, 255 * (1 - abs(3 * ratio - 1))))
    g = int(max(0, 255 * (1 - abs(3 * ratio - 2))))
    b = int(max(0, 255 * (1 - abs(3 * ratio - 3))))
    return (r, g, b)

def draw_square(screen, color, start, end):
    side = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
    x = start[0]
    y = start[1]
    pygame.draw.rect(screen, color, (x, y, side, side))

def draw_right_triangle(screen, color, start, end):
    pygame.draw.polygon(screen, color, [start, (start[0], end[1]), end])

def draw_equilateral_triangle(screen, color, start, end):
    base = end[0] - start[0]
    height = int((math.sqrt(3)/2) * abs(base))
    points = [
        (start[0], end[1]),
        (end[0], end[1]),
        ((start[0] + end[0]) // 2, end[1] - height)
    ]
    pygame.draw.polygon(screen, color, points)

def draw_rhombus(screen, color, start, end):
    mid_x = (start[0] + end[0]) // 2
    mid_y = (start[1] + end[1]) // 2
    points = [
        (mid_x, start[1]),
        (end[0], mid_y),
        (mid_x, end[1]),
        (start[0], mid_y)
    ]
    pygame.draw.polygon(screen, color, points)

def main():
    pygame.init()
    WIDTH, HEIGHT = 640, 480
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Shape Drawer")
    clock = pygame.time.Clock()

    color = (0, 0, 255)
    draw_mode = 'circle'
    drawing = False
    start_pos = None

    PALETTE_HEIGHT = 30
    palette_rect = pygame.Rect(0, HEIGHT - PALETTE_HEIGHT, WIDTH, PALETTE_HEIGHT)

    screen.fill((0, 0, 0))
    draw_palette(screen, HEIGHT - PALETTE_HEIGHT, WIDTH, PALETTE_HEIGHT)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_c:
                    draw_mode = 'circle'
                elif event.key == pygame.K_t:
                    draw_mode = 'rect'
                elif event.key == pygame.K_e:
                    draw_mode = 'eraser'
                elif event.key == pygame.K_q:
                    draw_mode = 'square'
                elif event.key == pygame.K_w:
                    draw_mode = 'right_triangle'
                elif event.key == pygame.K_e:
                    draw_mode = 'equilateral_triangle'
                elif event.key == pygame.K_r:
                    draw_mode = 'rhombus'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if palette_rect.collidepoint(event.pos):
                    x, _ = event.pos
                    color = get_color_from_palette(x, WIDTH)
                else:
                    start_pos = event.pos
                    drawing = True

            if event.type == pygame.MOUSEBUTTONUP:
                if drawing:
                    end_pos = event.pos
                    if draw_mode == 'circle':
                        pygame.draw.circle(screen, color, end_pos, 20)
                    elif draw_mode == 'rect':
                        x, y = start_pos
                        w, h = end_pos[0] - x, end_pos[1] - y
                        pygame.draw.rect(screen, color, pygame.Rect(x, y, w, h))
                    elif draw_mode == 'square':
                        draw_square(screen, color, start_pos, end_pos)
                    elif draw_mode == 'right_triangle':
                        draw_right_triangle(screen, color, start_pos, end_pos)
                    elif draw_mode == 'equilateral_triangle':
                        draw_equilateral_triangle(screen, color, start_pos, end_pos)
                    elif draw_mode == 'rhombus':
                        draw_rhombus(screen, color, start_pos, end_pos)
                    elif draw_mode == 'eraser':
                        pygame.draw.circle(screen, (0, 0, 0), end_pos, 20)
                    drawing = False

        draw_palette(screen, HEIGHT - PALETTE_HEIGHT, WIDTH, PALETTE_HEIGHT)
        pygame.display.flip()
        clock.tick(60)

main()
