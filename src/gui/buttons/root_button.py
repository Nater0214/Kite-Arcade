from typing import Any, Callable, Optional

import pygame


class Button(pygame.sprite.Sprite):
    """A button that can be pressed"""

    _on_click: Callable[[], Optional[Any]]
    image: pygame.Surface
    rect: pygame.Rect
    _base_image: pygame.Surface
    _hover_image: pygame.Surface
    _is_hovering: bool = False

    def __init__(
        self,
        coords: tuple[int, int],
        dimensions: tuple[int, int],
        text: str,
        on_click: Callable[[], Optional[Any]] = lambda: None,
        font_name: Optional[str] = None,
        font_size: int = 24,
        color: pygame.Color = pygame.Color((16, 16, 16)),
        hover_color: pygame.Color = pygame.Color((64, 64, 64)),
        font_color: pygame.Color = pygame.Color((192, 192, 192)),
    ) -> None:
        # Call super init
        super().__init__()

        # Set instance variables
        self._on_click = on_click

        # Font and text stuff
        try:
            font = pygame.font.Font(font_name, font_size)
        except FileNotFoundError:
            font = pygame.font.SysFont(font_name, font_size)

        text_surface = font.render(text, True, font_color)

        # Create button surfaces
        self._base_image = pygame.Surface(dimensions)
        self._base_image.fill(color)

        self._hover_image = pygame.Surface(dimensions)
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
        mouse_pos = pygame.mouse.get_pos()
        is_currently_hovering = self.rect.collidepoint(mouse_pos)
        if is_currently_hovering != self._is_hovering:
            self._is_hovering = is_currently_hovering
            self.image = (
                self._hover_image if is_currently_hovering else self._base_image
            )

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self._on_click()
