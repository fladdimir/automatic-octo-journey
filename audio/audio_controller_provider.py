import platform
from typing import Callable

from audio.audio_controller import AudioController


def create_audio_controller_provider() -> Callable[[], AudioController]:

    if platform.system() == "Linux":
        from audio.ubuntu_audio_controller import UbuntuAudioController

        return UbuntuAudioController

    elif platform.system() == "Windows":
        from audio.windows_audio_controller import WindowsAudioController

        singleton = WindowsAudioController()
        return lambda: singleton

    else:
        raise NotImplementedError(f"system {platform.system()} not supported")
