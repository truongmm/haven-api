from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# Initialize App
app = Flask(__name__)
app.config.from_object('config')
app.debug = True

# Initialize Database
db = SQLAlchemy(app)
db.create_all()

from app import models, views
