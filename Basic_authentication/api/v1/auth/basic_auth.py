#!/usr/bin/env python3
""" Auth Class
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Auth Class
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ extract_base64_authorization_header
        """
        if not authorization_header or type(authorization_header) != str:
            return None
        if authorization_header[:6] != 'Basic ':
            return None
        return authorization_header[6:]
