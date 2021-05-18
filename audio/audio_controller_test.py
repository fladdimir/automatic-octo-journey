from audio.audio_controller_provider import create_audio_controller_provider


def test_audio_controller():

    audio_controller = create_audio_controller_provider()()

    initial_volume = audio_controller.get_level()
    assert 0 <= initial_volume <= 1

    audio_controller.set_level(1.1)
    assert audio_controller.get_level() == 1.0

    audio_controller.set_level(-0.7)
    assert audio_controller.get_level() == 0

    audio_controller.set_level(initial_volume)
