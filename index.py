from app import start_app, socketio
from flask import render_template
from app.helpers import status

app = start_app()

@app.route("/")
def index():
    if status.is_open():
        return render_template("open.html")
    else:
        return render_template("closed.html")

if __name__ == "__main__":
    socketio.run(app)