import platform

import pytest

from audio.audio_controller import AudioController


@pytest.mark.skipif(platform.system() != "Linux", reason="test for ubuntu")
def test_ubuntu_audio():
    from audio.ubuntu_audio_controller import UbuntuAudioController

    audio_controller: AudioController = UbuntuAudioController()

    initial_volume = audio_controller.get_level()
    assert 0 <= initial_volume <= 1

    audio_controller.set_level(1.1)
    assert audio_controller.get_level() == 1.0

    audio_controller.set_level(-0.7)
    assert audio_controller.get_level() == 0

    audio_controller.set_level(initial_volume)
