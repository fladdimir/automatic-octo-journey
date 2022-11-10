# https://pynput.readthedocs.io/en/latest/mouse.html#controlling-the-mouse

from pynput.mouse import Button, Controller

from mouse.mouse_controller import MouseController


class PynputMouseController(MouseController):
    def __init__(self) -> None:
        super().__init__()
        self._mouse = Controller()

    def move(self, x: float, y: float) -> None:
        self._mouse.move(x, -y)

    def click(self) -> None:
        self._mouse.click(Button.left)
