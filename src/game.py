import pygame

from .gui.buttons import Button


def run() -> None:
    """
    Run the main game
    """

    # Initialize the game
    pygame.init()
    pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Kite Arcade")

    # Create buttons
    test_button = Button(
        (10, 10),
        (100, 50),
        "Quit",
        lambda: pygame.event.post(pygame.event.Event(pygame.QUIT)),
    )

    # Create the buttons sprite group
    all_buttons: pygame.sprite.Group[Button] = pygame.sprite.Group()
    all_buttons.add(test_button)

    # Run the game loop
    done = False
    while not done:
        # Handle events
        events = pygame.event.get()
        all_buttons.update(events)
        for event in events:
            if event.type == pygame.QUIT:
                done = True
            for button in all_buttons:
                button.handle_event(event)

        # Update the display
        all_buttons.draw(pygame.display.get_surface())
        pygame.display.update()

    # Quit the game
    pygame.quit()
