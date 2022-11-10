from os import getenv

from mouse.mouse_controller import MouseController


def get_mouse_controller() -> MouseController:

    if getenv("WAYLAND_DISPLAY") is not None:
        print("wayland detected, using uinput-mouse")
        from mouse.uinput_mouse import UinputMouseController

        return UinputMouseController()

    else:
        print("using pynput-mouse")
        from mouse.pynput_mouse import PynputMouseController

        return PynputMouseController()
