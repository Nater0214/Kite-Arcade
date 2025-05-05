import pygame as pg

from .game_input.event import InputEvent, InputEventAction, InputEventCode
from .game_input.methods import KeyboardInputMethod, keyboard
from .gui import NavigationGrid
from .gui.buttons import Button


def run() -> None:
    """
    Run the main game
    """

    # Initialize the game
    pg.init()
    pg.display.set_mode((600, 400))
    pg.display.set_caption("Kite Arcade")

    # Add the input methods
    p1_input_method = KeyboardInputMethod(keyboard.WASD_MAPPING)
    p2_input_method = KeyboardInputMethod(keyboard.IJKL_MAPPING)

    # Create buttons
    start_one_player_button = Button(
        (200, 50),
        (200, 50),
        "One Player",
        lambda: print("One Player"),
    )
    start_two_player_versus_button = Button(
        (200, 150),
        (200, 50),
        "Two Player Versus",
        lambda: print("Two Player Versus"),
    )
    start_two_player_coop_button = Button(
        (200, 250),
        (200, 50),
        "Two Player Coop",
        lambda: print("Two Player Coop"),
    )

    # Create the buttons sprite group
    all_buttons: pg.sprite.Group[Button] = pg.sprite.Group()
    all_buttons.add(start_one_player_button)
    all_buttons.add(start_two_player_versus_button)
    all_buttons.add(start_two_player_coop_button)

    # Create the navigation grid
    navigation_grid = NavigationGrid((1, 3))
    navigation_grid.set_element(start_one_player_button, (0, 0))
    navigation_grid.set_element(start_two_player_versus_button, (0, 1))
    navigation_grid.set_element(start_two_player_coop_button, (0, 2))

    # Run the game loop
    done = False
    while not done:
        # Handle events
        events = pg.event.get()
        all_buttons.update(events)
        for event in events:
            if event.type == pg.QUIT:
                done = True
            for button in all_buttons:
                button.handle_event(event)
            p1_input_method.handle_event(event)
            p2_input_method.handle_event(event)

        # Handle input
        for input_event in p1_input_method.events():
            if input_event.action == InputEventAction.PRESS:
                match input_event.code:
                    case InputEventCode.UP:
                        navigation_grid.navigate_up()
                    case InputEventCode.DOWN:
                        navigation_grid.navigate_down()
                    case InputEventCode.LEFT:
                        navigation_grid.navigate_left()
                    case InputEventCode.RIGHT:
                        navigation_grid.navigate_right()
                    case InputEventCode.BUTTON1:
                        navigation_grid.click()

        # Update the display
        all_buttons.draw(pg.display.get_surface())
        pg.display.flip()

    # Quit the game
    pg.quit()
