from typing import Any, Callable, Optional

import pygame as pg

from src.gui.element import Element


class Button(Element, pg.sprite.Sprite):
    """A button that can be pressed"""

    _on_click: Callable[[], Optional[Any]]
    image: pg.Surface
    rect: pg.Rect
    _base_image: pg.Surface
    _hover_image: pg.Surface
    _is_hovering: bool = False

    def __init__(
        self,
        coords: tuple[int, int],
        dimensions: tuple[int, int],
        text: str,
        on_click: Callable[[], Optional[Any]] = lambda: None,
        font_name: Optional[str] = None,
        font_size: int = 24,
        color: pg.Color = pg.Color((16, 16, 16)),
        hover_color: pg.Color = pg.Color((64, 64, 64)),
        font_color: pg.Color = pg.Color((192, 192, 192)),
    ) -> None:
        # Call super init
        super(Element, self).__init__()
        super(pg.sprite.Sprite, self).__init__()

        # Set instance variables
        self._on_click = on_click

        # Font and text stuff
        try:
            font = pg.font.Font(font_name, font_size)
        except FileNotFoundError:
            font = pg.font.SysFont(font_name, font_size)

        text_surface = font.render(text, True, font_color)

        # Create button surfaces
        self._base_image = pg.Surface(dimensions)
        self._base_image.fill(color)

        self._hover_image = pg.Surface(dimensions)
        self._hover_image.fill(hover_color)

        # Set initial surface and rect
        self.image = self._base_image
        self.rect = self.image.get_rect(topleft=coords)

        # Draw text to surfaces
        text_rect = text_surface.get_rect()
        text_rect.center = (dimensions[0] // 2, dimensions[1] // 2)
        self._base_image.blit(text_surface, text_rect)
        self._hover_image.blit(text_surface, text_rect)

    def update(self, *args, **kwargs) -> None:
        self.image = self._base_image if not self._is_hovering else self._hover_image

    def update_hovering(self, hovering: bool) -> None:
        self._is_hovering = hovering

    def handle_event(self, event: pg.event.Event) -> None:
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self._on_click()

    def click(self) -> None:
        self._on_click()
