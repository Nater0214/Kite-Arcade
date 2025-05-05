import pygame as pg

from ..event import InputEvent, InputEventAction, InputEventCode
from . import InputMethod


WASD_MAPPING = {
    pg.K_w: InputEventCode.UP,
    pg.K_a: InputEventCode.LEFT,
    pg.K_s: InputEventCode.DOWN,
    pg.K_d: InputEventCode.RIGHT,
    pg.K_e: InputEventCode.BUTTON1,
    pg.K_q: InputEventCode.BUTTON2,
}

WASD_SOUTHPAW_MAPPING = {
    pg.K_w: InputEventCode.UP,
    pg.K_a: InputEventCode.LEFT,
    pg.K_s: InputEventCode.DOWN,
    pg.K_d: InputEventCode.RIGHT,
    pg.K_q: InputEventCode.BUTTON1,
    pg.K_e: InputEventCode.BUTTON2,
}

IJKL_MAPPING = {
    pg.K_i: InputEventCode.UP,
    pg.K_j: InputEventCode.LEFT,
    pg.K_k: InputEventCode.DOWN,
    pg.K_l: InputEventCode.RIGHT,
    pg.K_o: InputEventCode.BUTTON1,
    pg.K_u: InputEventCode.BUTTON2,
}

IJKL_SOUTHPAW_MAPPING = {
    pg.K_i: InputEventCode.UP,
    pg.K_j: InputEventCode.LEFT,
    pg.K_k: InputEventCode.DOWN,
    pg.K_l: InputEventCode.RIGHT,
    pg.K_u: InputEventCode.BUTTON1,
    pg.K_o: InputEventCode.BUTTON2,
}


class KeyboardInputMethod(InputMethod):
    """
    An input method using the keyboard
    """

    _mapping: dict[int, InputEventCode]

    def __init__(self, mapping: dict[int, InputEventCode]) -> None:
        super().__init__()
        self._mapping = mapping

    def handle_event(self, event: pg.event.Event) -> None:
        """
        Handle an event
        """

        if event.type == pg.KEYDOWN:
            if event.key in self._mapping:
                self._event_queue.append(
                    InputEvent(self._mapping[event.key], InputEventAction.PRESS)
                )
        elif event.type == pg.KEYUP:
            if event.key in self._mapping:
                self._event_queue.append(
                    InputEvent(self._mapping[event.key], InputEventAction.RELEASE)
                )
