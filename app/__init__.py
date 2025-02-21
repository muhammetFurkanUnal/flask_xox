from flask import Flask
from flask_cors import CORS

from .routes import XOX_engine_BP


def create_app():
    app = Flask(__name__)
    
    CORS(app)
    
    app.secret_key = "secretkey"
    
    app.register_blueprint(XOX_engine_BP)

    return app


