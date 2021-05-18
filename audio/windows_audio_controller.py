from audio.helper import bound_value
from audio.audio_controller import AudioController

from ctypes import POINTER, cast

from comtypes import CLSCTX_ALL

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


class WindowsAudioController(AudioController):
    def __init__(self) -> None:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.volume = cast(interface, POINTER(IAudioEndpointVolume))

    def get_level(self) -> float:
        return self.volume.GetMasterVolumeLevelScalar()

    def set_level(self, level: float) -> None:
        bounded = bound_value(level, 0, 1)
        self.volume.SetMasterVolumeLevelScalar(bounded, None)
