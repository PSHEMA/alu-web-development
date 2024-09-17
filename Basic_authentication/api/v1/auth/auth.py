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
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path = f'{path}/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user
        """
        return None
