from .. import socketio
from flask_socketio import send
from flask import Blueprint
from ..helpers import status
from .server import serverHandler

bp = Blueprint("socket", __name__)

def emit_status():
    socketio.emit("sv_status", { "status": serverHandler.is_open() })

@socketio.on("connect")
def handle_connect():
    print("User connected")
    emit_status()

@socketio.on("status_request")
def handle_status_request():
    emit_status()

@socketio.on("open_request")
def handle_open():
    print("\nOpen server request received\n")
    if not status.is_open():
        serverHandler.start_server()
        emit_status()

@socketio.on("shutdown_request")
def handle_shutdown():
    if status.is_open():
        serverHandler.shut_down()

def send_console(message):
    socketio.emit("mc_console_msg", { "msg": message })