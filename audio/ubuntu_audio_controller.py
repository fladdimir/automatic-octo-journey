import alsaaudio

from audio.audio_controller import AudioController
from audio.helper import bound_value


class UbuntuAudioController(AudioController):
    def __init__(self) -> None:
        super().__init__()
        mixers = alsaaudio.mixers()
        self.mixer = alsaaudio.Mixer(mixers[0])

    def get_level(self) -> float:
        vols = self.mixer.getvolume()
        int_vol = int(vols[0])
        return self._percentage_points_to_float(int_vol)

    def set_level(self, level: float) -> None:
        int_volume = self._float_to_percentage_points(level)
        self.mixer.setvolume(int_volume)

    def _float_to_percentage_points(self, float_value: float) -> int:
        bounded = bound_value(float_value, 0, 1)
        return int(bounded * 100.0)

    def _percentage_points_to_float(self, pp: int) -> float:
        bounded = bound_value(pp, 0, 100)
        return bounded / 100.0
