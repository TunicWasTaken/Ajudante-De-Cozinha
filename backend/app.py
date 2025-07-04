from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import AppConfig

app = Flask(__name__)

CORS(app, supports_credentials=True)
JWTManager(app)
app.config.from_object(AppConfig)

import routes

if __name__ == "__main__":
    app.run(debug=True)
