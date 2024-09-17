#!/usr/bin/env python3
""" Auth Class
"""

from platform import node
from typing import TypeVar
from flask import request


class Auth():
    """ Auth Class
    """

    def require_auth(self, path: str, excluded_paths: list) -> bool:
        """ require_auth
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ authorization_header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user
        """
        return None
