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
def index():
    return app.send_static_file("index.html")


@app.route("/volume", methods=["GET", "POST"])
def volume() -> str:
    if request.method == "GET":
        return str(audio_controller_provider().get_level())
    elif request.method == "POST":
        new_value = float(request.args.get("new_value"))
        audio_controller_provider().set_level(new_value)
        return str(audio_controller_provider().get_level())


@app.route("/change_volume", methods=["POST"])
def change_volume() -> str:
    change_by = float(request.args.get("by"))
    current_volume = audio_controller_provider().get_level()
    audio_controller_provider().set_level(current_volume + change_by)
    current_volume = audio_controller_provider().get_level()
    print(f"current volume: {current_volume}")
    return str(current_volume)


app.run("0.0.0.0", 5000, debug=True)
