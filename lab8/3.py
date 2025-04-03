import pygame

def get_color_from_palette(x, width):
    """Get RGB color from a horizontal gradient palette."""
    ratio = x / width
    r = int(max(0, 255 * (1 - abs(3 * ratio - 1))))
    g = int(max(0, 255 * (1 - abs(3 * ratio - 2))))
    b = int(max(0, 255 * (1 - abs(3 * ratio - 3))))
    return (r, g, b)

def draw_palette(screen, y, width, height):
    """Draws a horizontal gradient palette at position y."""
    for x in range(width):
        color = get_color_from_palette(x, width)
        pygame.draw.rect(screen, color, (x, y, 1, height))

def main():
    pygame.init()
    WIDTH, HEIGHT = 640, 480
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Drawing App with Color Picker")
    clock = pygame.time.Clock()

    color = (0, 0, 255)
    radius = 10
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
            # Changes the drawing mode based on the key pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_c:
                    draw_mode = 'circle'
                elif event.key == pygame.K_e:
                    draw_mode = 'eraser'
                elif event.key == pygame.K_t:
                    draw_mode = 'rect'
            # triggered when any mouse button is pressed down, updates the current drawing color if it collides with the gradient
            if event.type == pygame.MOUSEBUTTONDOWN:
                if palette_rect.collidepoint(event.pos):
                    x, _ = event.pos
                    color = get_color_from_palette(x, WIDTH)
            # else, it starts drawing
                else:
                    start_pos = event.pos
                    drawing = True
            # this finishes the drawing process, if started prior. moreover, it helps us draw circles and rectangles, as well as the eraser
            if event.type == pygame.MOUSEBUTTONUP:
                if drawing:
                    end_pos = event.pos
                    if draw_mode == 'circle':
                        pygame.draw.circle(screen, color, end_pos, radius)
                    elif draw_mode == 'rect':
                        x, y = start_pos
                        w, h = end_pos[0] - x, end_pos[1] - y
                        pygame.draw.rect(screen, color, pygame.Rect(x, y, w, h))
                    elif draw_mode == 'eraser':
                        pygame.draw.circle(screen, (0, 0, 0), end_pos, radius)
                    drawing = False
            # tracks the current position of the mouse, and captures the dragging motion
            if event.type == pygame.MOUSEMOTION and drawing:
                pos = event.pos
                if draw_mode == 'circle':
                    pygame.draw.circle(screen, color, pos, radius)
                elif draw_mode == 'eraser':
                    pygame.draw.circle(screen, (0, 0, 0), pos, radius)

        # Redraw color picker every frame
        draw_palette(screen, HEIGHT - PALETTE_HEIGHT, WIDTH, PALETTE_HEIGHT)

        pygame.display.flip()
        clock.tick(60)

main()
