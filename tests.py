"""Tests for images repository"""

import unittest
import crud


def is_user1(name, email):
    """Is this user1?
    >>> is_user1("user1", "user0@test.com")
    True
    >>> is_user1("Jane", "jane@hacks.com")
    False
    >>> is_user1("user1", "banana@test.com")
    True
    >>> is_user1("Banana", "user0@test.com")
    True
    """
    return name == "user1" or email == "user0@test.com"