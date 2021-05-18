from audio.audio_controller_provider import create_audio_controller_provider
from flask import Flask, request

audio_controller_provider = create_audio_controller_provider()

app = Flask(__name__)


@app.route("/")
def index():
    return app.send_static_file("index.html")


def get_level_str() -> str:
    current_volume = audio_controller_provider().get_level()
    print(f"\ncurrent volume: {current_volume}")
    return str(current_volume)


@app.route("/volume", methods=["GET", "POST"])
def volume() -> str:
    if request.method == "GET":
        return get_level_str()
    elif request.method == "POST":
        new_value = float(request.args.get("new_value"))  # ?new_value=0.12
        audio_controller_provider().set_level(new_value)
        return get_level_str()


@app.route("/change_volume", methods=["POST"])
def change_volume() -> str:
    change_by = float(request.args.get("by"))  # ?by=-0.05
    current_volume = audio_controller_provider().get_level()
    audio_controller_provider().set_level(current_volume + change_by)
    return get_level_str()


app.run("0.0.0.0", 5000, debug=False)
