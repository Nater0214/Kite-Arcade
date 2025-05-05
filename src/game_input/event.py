from enum import Enum


__all__ = ["InputEventCode", "InputEventAction", "InputEvent"]


class InputEventCode(Enum):
    """
    A code for an input event
    """

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    BUTTON1 = 4
    BUTTON2 = 5


class InputEventAction(Enum):
    """
    An action an input event
    """

    PRESS = 0
    RELEASE = 1


class InputEvent:
    """
    An input event
    """

    _code: InputEventCode
    _action: InputEventAction

    def __init__(self, code: InputEventCode, action: InputEventAction) -> None:
        self._code = code
        self._action = action

    @property
    def code(self) -> InputEventCode:
        return self._code

    @property
    def action(self) -> InputEventAction:
        return self._action

    def __repr__(self) -> str:
        return f"InputEvent(code={self._code}, action={self._action})"
