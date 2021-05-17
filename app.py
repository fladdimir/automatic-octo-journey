import platform
from typing import Callable

from flask import Flask, request

from audio.audio_controller import AudioController

audio_controller_provider: Callable[[], AudioController]
if platform.system() == "Linux":
    from audio.ubuntu_audio_controller import UbuntuAudioController

    audio_controller_provider = UbuntuAudioController
elif platform.system() == "Windows":
    raise NotImplementedError("not yet available on Windows")
else:
    raise NotImplementedError(f"platform {platform.system()} not supported")


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"  #


@app.route("/volume", methods=["GET", "POST"])
def get_volume() -> str:
    if request.method == "GET":
        return str(audio_controller_provider().get_level())
    elif request.method == "POST":
        new_value = float(request.args.get("new_value"))
        audio_controller_provider().set_level(new_value)
        return str(audio_controller_provider().get_level())


app.run("0.0.0.0", 5000, debug=True)
