from flask import Flask, send_from_directory
from app.routes import routes
import os

app = Flask(__name__, static_folder="static", static_url_path="")
app.register_blueprint(routes)

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
