from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from config import Config
import os
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)
app.config.from_object(Config)

currentDirectory = os.getcwd()
databasePath = os.path.join(currentDirectory, "database.db")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + databasePath
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = "True"
db = SQLAlchemy(app)

import routes, models
