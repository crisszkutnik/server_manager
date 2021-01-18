from app import start_app, socketio
from flask import render_template
from app.helpers import status

app = start_app()

@app.route("/")
def index():
    return render_template("page.html", open=status.is_open())

if __name__ == "__main__":
    socketio.run(app)