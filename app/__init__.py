"""Main setup code for Mercator.
"""

from flask import Flask
from flask.ext.security import Security
from flask.ext.security import SQLAlchemyUserDatastore
from flask.ext.sqlalchemy import SQLAlchemy

# Set up flask
app = Flask(__name__)
app.config.from_pyfile("config.py")

# Set up flask-SQLAlchemy
db = SQLAlchemy(app)

# Set up flask-security
from .models.security import Role
from .models.security import User

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

