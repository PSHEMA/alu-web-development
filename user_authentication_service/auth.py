#!/usr/bin/env python3
""" Auth
"""
import bcrypt
from user import User


def _hash_password(password: str) -> str:
    """ Hash password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
