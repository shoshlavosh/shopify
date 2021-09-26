"""CRUD operations"""

from model import db, User, Image, app, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    #check to see if email and password are the correct data types 
    #before adding user to the database
    assert type(email) == str
    assert type(password) == str

    db.session.add(user)
    db.session.commit()

    return user


def get_users():
    """Return all users."""

    return User.query.all()


def print_users():
    """Print all users in the database"""

    users = get_users()

    for user in users:
        print(user)


def get_user_by_id(user_id):
    """Return a user by their user id"""

    return User.query.get(user_id)


def create_image(image_name, image_description,
            date_added, size_in_mb):

    image = Image(image_name=image_name, image_description=image_description,
            date_added=date_added, size_in_mb=size_in_mb)

    #check to see if image name, description, and size are the correct 
    #data types before adding image to the database
    assert type(image_name) == str
    assert type(image_description) == str
    assert type(size_in_mb) == int

    db.session.add(image)
    db.session.commit()

    return image


def get_images():
    """Return all images"""

    return Image.query.all()


def image_search(keyword):
    """Return an image by keyword"""

    images = get_images()

    for image in images:
        if keyword in image.image_description or keyword in image.image_name:
            return image


def print_all_images():
    """Print all images in the database"""

    images = get_images()

    for image in images:
        print(image)


if __name__ == '__main__':
    connect_to_db(app)