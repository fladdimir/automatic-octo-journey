class AudioController:
    def __init__(self) -> None:
        super().__init__()

    def increase(self) -> None:
        raise NotImplementedError()

    def decrease(self) -> None:
        raise NotImplementedError()
