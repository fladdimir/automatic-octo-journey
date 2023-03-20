import os
import pwd
import subprocess

from audio.audio_controller import AudioController


class UbuntuAudioController(AudioController):
    def __init__(self) -> None:
        super().__init__()

    def increase(self) -> None:
        self._change(True)

    def decrease(self) -> None:
        self._change(False)

    def _change(self, increase: bool) -> None:
        suffix = "+" if increase else "-"
        cmd = "amixer -D pulse sset Master 5%" + suffix
        uid = self._get_user_id()
        subprocess.run(cmd, shell=True, check=True, user=uid)

    def _get_user_id(self) -> int:
        current_user = os.getuid()
        if current_user != 0:
            return current_user  # non-root
        user_name = os.getenv("SUDO_USER")
        pwnam = pwd.getpwnam(user_name)
        return pwnam.pw_uid
