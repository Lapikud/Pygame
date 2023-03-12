import pygame
pygame.init()

# create a window
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()

running = True
while running:

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # closing window finishes game loop
            running = False

    # Draw

    # Update screen
    pygame.display.flip()

    # FPS
    clock.tick(30)
