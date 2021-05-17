class AudioController:
    def __init__(self) -> None:
        """init"""
        super().__init__()

    def get_level(self) -> float:
        """return the current audio level (range from 0 to 1)"""
        raise NotImplementedError()

    def set_level(self, level: float) -> None:
        """set the audio level to a given value between 0 and 1"""
        raise NotImplementedError()
