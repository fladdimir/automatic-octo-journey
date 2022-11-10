import grp
import os
import pwd

import uinput

from mouse.mouse_controller import MouseController


class UinputMouseController(MouseController):
    def __init__(self) -> None:
        super().__init__()

        self.device = uinput.Device(  # requires root privileges
            [
                uinput.BTN_LEFT,
                uinput.REL_X,
                uinput.REL_Y,
            ]
        )
        # TODO:

    def move(self, x: float, y: float) -> None:
        self.device.emit(uinput.REL_X, int(x), syn=False)
        self.device.emit(uinput.REL_Y, int(-y))

    def click(self) -> None:
        # emit_click does not work https://github.com/tuomasjjrasanen/python-uinput/issues/26
        self.device.emit(uinput.BTN_LEFT, 1)
        self.device.emit(uinput.BTN_LEFT, 0)

    def _drop_privileges():
        # https://stackoverflow.com/questions/2699907/dropping-root-permissions-in-python
        if os.getuid() != 0:
            return  # We're not root so, like, whatever dude

        # Get the uid/gid from the name
        user_name = os.getenv("SUDO_USER")
        pwnam = pwd.getpwnam(user_name)

        # Remove group privileges
        os.setgroups([])

        # Try setting the new uid/gid
        os.setgid(pwnam.pw_gid)
        os.setuid(pwnam.pw_uid)

        # Ensure a reasonable umask
        os.umask(0o22)
