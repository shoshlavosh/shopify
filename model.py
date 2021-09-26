"""Models for image repository"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 
db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        """Show info about user"""
        return f'<User user_id={self.user_id} email={self.email}>'


class Image(db.Model):
    """An image"""

    __tablename__ = 'images'

    image_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'))
    image_name = db.Column(db.String)
    image_description = db.Column(db.String)
    date_added = db.Column(db.DateTime)
    size_in_mb = db.Column(db.Integer)

    def __repr__(self):
        """Show info about image"""
        return f'<Image image_id={self.image_id} image_name={self.image_name} image_description={self.image_description}>'


def connect_to_db(app, db_uri="postgresql:///images", echo=True):
    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_ECHO"] = echo
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)

    print("Connected to the db!")


if __name__ == '__main__':
    connect_to_db(app)