from flask import Flask, request

from audio.audio_controller_provider import create_audio_controller_provider
from mouse import mouse
from keys import keys

audio_controller_provider = create_audio_controller_provider()

app = Flask(__name__)

# static
@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/static/<path>")
def static_file(path):
    return app.send_static_file(path)


# audio
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


# mouse
@app.route("/change_cursor_pos", methods=["POST"])
def change_cursor_pos() -> str:
    x = float(request.args.get("x"))  # ?x=20
    y = float(request.args.get("y"))  # ?y=20
    mouse.move(x, y)
    return "ok"


@app.route("/click", methods=["POST"])
def click() -> str:
    mouse.click()
    return "ok"


@app.route("/type", methods=["POST"])
def type() -> str:
    content = str(request.args.get("content"))
    keys.tap(content)
    return content


# run
app.run("0.0.0.0", 5000, debug=False)
