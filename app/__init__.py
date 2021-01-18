from eventlet import monkey_patch
monkey_patch()

from flask import Flask
from flask_socketio import SocketIO
from .src.server import serverHandler

socketio = SocketIO()

def start_app():
    app = Flask(__name__)

    from .src.events import bp
    app.register_blueprint(bp)

    socketio.init_app(app)

    return app