"""CRUD operations"""

from model import db, User, Image, app, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Returns a user by their user id"""

    return User.query.get(user_id)


def create_image(image_name, image_description,
            date_added, size_in_mb):

    image = Image(image_name=image_name, image_description=image_description,
            date_added=date_added, size_in_mb=size_in_mb)

    db.session.add(image)
    db.session.commit()

    return image


def get_images():
    """Returns all images"""

    return Image.query.all()


if __name__ == '__main__':
    connect_to_db(app)