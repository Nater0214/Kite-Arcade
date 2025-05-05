import numpy as np
import numpy.typing as npt

from .element import Element


class NavigationGrid:
    """
    A class that stores how buttons will be selected when navigating
    """

    _elements: npt.NDArray[np.object_ | np.void]
    _pointer: npt.NDArray[np.uint32]

    def __init__(
        self, dimensions: tuple[int, int], start_coords: tuple[int, int] = (0, 0)
    ) -> None:
        self._elements = np.full(dimensions, None)
        self._pointer = np.array(list(start_coords), dtype=np.uint32)

    def set_element(self, element: Element, coords: tuple[int, int]) -> None:
        self._elements[coords] = element
        if self._pointer[0] == coords[0] and self._pointer[1] == coords[1]:
            self._elements[*self._pointer].update_hovering(True)

    def navigate_up(self) -> None:
        if self._pointer[1] != 0:
            if self._elements[*self._pointer] is not None:
                self._elements[*self._pointer].update_hovering(False)
            self._pointer[1] -= 1
            if self._elements[*self._pointer] is not None:
                self._elements[*self._pointer].update_hovering(True)

    def navigate_down(self) -> None:
        if self._pointer[1] != self._elements.shape[1] - 1:
            if self._elements[*self._pointer] is not None:
                self._elements[*self._pointer].update_hovering(False)
            self._pointer[1] += 1
            if self._elements[*self._pointer] is not None:
                self._elements[*self._pointer].update_hovering(True)

    def navigate_left(self) -> None:
        if self._pointer[0] != 0:
            if self._elements[*self._pointer] is not None:
                self._elements[*self._pointer].update_hovering(False)
            self._pointer[0] -= 1
            if self._elements[*self._pointer] is not None:
                self._elements[*self._pointer].update_hovering(True)

    def navigate_right(self) -> None:
        if self._pointer[0] != self._elements.shape[0] - 1:
            if self._elements[*self._pointer] is not None:
                self._elements[*self._pointer].update_hovering(False)
            self._pointer[0] += 1
            if self._elements[*self._pointer] is not None:
                self._elements[*self._pointer].update_hovering(True)

    def click(self) -> None:
        self._elements[*self._pointer].click()
