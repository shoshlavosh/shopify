"""Tests"""

import unittest
import crud


def is_user1(name, email):
    """Is this user1?
    >>> is_user1("user1", "user0@test.com")
    True
    >>> is_user1("Jane", "jane@hacks.com")
    False
    >>> is_user1("USER1", "USER0@test.COM")
    True
    >>> is_user1("User1", "User@Test.Com")
    False
    >>> is_user1("User1", "User0@Test.Com")
    True
    """
    
    if name.lower() == "user1" and email.lower() == "user0@test.com":
        return True

    else:
        return False

#to run "is_user1()" test, enter the following in the command line: 
#$ python3 -m doctest -v tests.py