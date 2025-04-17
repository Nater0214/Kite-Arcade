import pygame


def run() -> None:
    """
    Run the main game
    """

    # Initialize the game
    pygame.init()
    pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Kite Arcade")

    # Run the game loop
    done = False
    while not done:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Update the display
        pygame.display.update()

    # Quit the game
    pygame.quit()
