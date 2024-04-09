from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

currentDirectory = os.getcwd()
databasePath = os.path.join(currentDirectory, "database.db")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + databasePath
db = SQLAlchemy(app)
import routes, models

