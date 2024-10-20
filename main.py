import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
        
    # Setting fps to 60
    clock = pygame.time.Clock()
    dt = 0
    
    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        dt = clock.tick(60) / 1000  # Update dt each frame

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Update the display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
