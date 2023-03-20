import platform
from typing import Callable

from audio.audio_controller import AudioController


def create_audio_controller_provider() -> Callable[[], AudioController]:

    if platform.system() == "Linux":
        from audio.ubuntu_audio_controller import UbuntuAudioController

        instance = UbuntuAudioController()
        return lambda: instance

    elif platform.system() == "Windows":
        from audio.windows_audio_controller import WindowsAudioController

        instance = WindowsAudioController()
        return lambda: instance

    else:
        raise NotImplementedError(f"system {platform.system()} not supported")
