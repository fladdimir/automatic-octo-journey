# https://pynput.readthedocs.io/en/latest/mouse.html#controlling-the-mouse

from pynput.mouse import Button, Controller

_mouse = Controller()


def move(x: float, y: float) -> None:
    _mouse.move(x, -y)


def click() -> None:
    _mouse.click(Button.left)
