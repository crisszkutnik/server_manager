from flask import Flask
from flask_socketio import SocketIO
from .src.server import serverHandler

socketio = SocketIO()

def start_app():
    app = Flask(__name__)

    from .src.socket import bp
    app.register_blueprint(bp)

    socketio.init_app(app)

    return app

serverHandler.start_server()