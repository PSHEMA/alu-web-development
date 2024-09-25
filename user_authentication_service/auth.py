#!/usr/bin/env python3
""" Auth
"""
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> str:
    """ Hash password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Initialize a new Auth instance.
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a user
        """
        if self._db.find_user_by(email=email) is not None:
            raise ValueError("User {email} already exists")
        new_user = self._db.add_user(email, _hash_password(password))
        return new_user
