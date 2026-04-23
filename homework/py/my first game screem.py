import pygame
pygame.init()
# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Game Screen")
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Fill the background with white
    
    # Update the display
    pygame.display.flip()
# Quit Pygame
pygame.quit()