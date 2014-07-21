"""Models for flask-security, authentication, etc.
"""

from flask.ext.security import RoleMixin
from flask.ext.security import UserMixin

from app import db
from .associationtables import roles_users

class Role(db.Model, RoleMixin):
    """A flask-security user role.

    Attributes:
        id (int): The role's ID.
        name (str): The name of this role.
        description (str): A description of this role.
        users (list of Users): A list of users that have this role.
    """
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    """A flask-security user.

    Attributes:
        id (int): The user's ID.
        email (str): The user's email.
        password (str): The user's password.
        active (boolean): If the user is marked as active.
        confirmed_at (DateTime): When the user confirmed their account.
        roles (list of Roles): A list of roles this user has.
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

