"""Tests for images repository"""

import unittest
import crud
import seed
from model import User, Image, app, db

class FlaskTests(unittest.TestCase):

    def setUp(self):
        """Set up that runs before every test"""

        self.client = app.test_client() #uses Flask test client
        app.config['TESTING'] = True

    def tearDown(self):
        """Tear down that runs after every test"""

        db.session.close()
        db.drop_all() 


def is_user1(name, email):
    """Is this user1?
    >>> is_user1("user1", "user0@test.com")
    True
    >>> is_user1("Jane", "jane@hacks.com")
    False
    >>> is_user1("user1", "banana@test.com")
    False
    >>> is_user1("Banana", "user0@test.com")
    False
    """
    
    if name == "user1" and email == "user0@test.com":
        return True

    else:
        return False

#to run "is_user1()" test, enter the following in the command line: 
#$ python3 -m doctest -v tests.py



if __name__ == '__main__':
    unittest.main()
