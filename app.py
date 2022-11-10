from os import getenv

from dotenv import load_dotenv
from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash, generate_password_hash

from audio.audio_controller_provider import create_audio_controller_provider
from keys import keys
from mouse.mouse_controller_provider import get_mouse_controller

load_dotenv()

audio_controller_provider = create_audio_controller_provider()
mouse = get_mouse_controller()


app = Flask(__name__)
auth = HTTPBasicAuth()

USER = getenv("PY_REMOTE_CONTROL_USER", "user")
PASSWORD = generate_password_hash(getenv("PY_REMOTE_CONTROL_PASSWORD", "password"))


@auth.verify_password
def verify_password(username, password):
    if username == USER and check_password_hash(PASSWORD, password):
        return username


# static
@app.route("/")
@auth.login_required
def index():
    return app.send_static_file("index.html")


@app.route("/static/<path>")
@auth.login_required
def static_file(path):
    return app.send_static_file(path)


# audio
def get_level_str() -> str:
    current_volume = audio_controller_provider().get_level()
    print(f"\ncurrent volume: {current_volume}")
    return str(current_volume)


@app.route("/volume", methods=["GET", "POST"])
@auth.login_required
def volume() -> str:
    if request.method == "GET":
        return get_level_str()
    elif request.method == "POST":
        new_value = float(request.args.get("new_value"))  # ?new_value=0.12
        audio_controller_provider().set_level(new_value)
        return get_level_str()


@app.route("/change_volume", methods=["POST"])
@auth.login_required
def change_volume() -> str:
    change_by = float(request.args.get("by"))  # ?by=-0.05
    current_volume = audio_controller_provider().get_level()
    audio_controller_provider().set_level(current_volume + change_by)
    return get_level_str()


# mouse
@app.route("/change_cursor_pos", methods=["POST"])
@auth.login_required
def change_cursor_pos() -> str:
    x = float(request.args.get("x"))  # ?x=20
    y = float(request.args.get("y"))  # ?y=20
    mouse.move(x, y)
    return "ok"


@app.route("/click", methods=["POST"])
@auth.login_required
def click() -> str:
    mouse.click()
    return "ok"


@app.route("/type", methods=["POST"])
@auth.login_required
def type_key() -> str:
    content = str(request.args.get("content"))
    keys.tap(content)
    return content


# run
app.run("0.0.0.0", 5000, debug=False)
