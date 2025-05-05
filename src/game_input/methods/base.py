from collections import deque
from typing import Iterable

import pygame as pg

from ..event import InputEvent


class InputMethod:
    """
    The base input method that can be inherited from.

    This class provides the groundwork for an input method.
    """

    _event_queue: deque[InputEvent]

    def __init__(self) -> None:
        self._event_queue = deque()

    def handle_event(self, event: pg.event.Event) -> None:
        raise NotImplementedError("handle_event not implemented for this input method!")

    def events(self) -> Iterable[InputEvent]:
        """
        Get the events from the event queue.

        This method will return an iterator of events from the event queue.
        The event queue will be cleared after the events have been returned.
        """

        events = self._event_queue.copy()
        self._event_queue.clear()
        return events
