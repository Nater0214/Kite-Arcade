class Element:
    _hovering: bool

    def __init__(self) -> None:
        super().__init__()
        self._hovering = False

    @property
    def hovering(self) -> bool:
        return self._hovering

    def update_hovering(self, hovering: bool) -> None:
        raise NotImplementedError("update_hovering not implemented for this element!")

    def click(self) -> None:
        raise NotImplementedError("click not implemented for this element!")
