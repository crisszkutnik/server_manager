from .. import socketio
from flask_socketio import send
from flask import Blueprint

bp = Blueprint("socket", __name__)


@socketio.on("connect")
def handle_connect():
    print("User connected")
    send("Hello user")