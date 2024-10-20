import pygame
from constants import *
from player import Player  # Ensure this import is correctly placed

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
        
    # Setting fps to 60
    clock = pygame.time.Clock()
    
    # Create a Player object in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 20)  # 20 is the radius
    
    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        dt = clock.tick(60) / 1000  # Update dt each frame

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Draw the player
        player.draw(screen)  # Render the player on the screen

        # Update the display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
