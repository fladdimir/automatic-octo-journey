from pynput.keyboard import Controller, Key

_keyboard = Controller()

special_keys = {"\n": Key.enter, "Backspace": Key.backspace}


def tap(keys: str) -> None:
    value = special_keys.get(keys, keys)
    _keyboard.tap(value)
