from flask import Flask, send_from_directory
from .routes import routes  
import os

def create_app():
    app = Flask(
        __name__,
        static_folder=os.path.join(os.path.dirname(__file__), '..', 'static'),
        static_url_path=''
    )
    app.register_blueprint(routes)  

    @app.route('/')
    def index():
        return send_from_directory(app.static_folder, 'index.html')

    return app
