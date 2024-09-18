#!/usr/bin/env python3
""" Auth Class
"""
import base64
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Auth Class
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ extract_base64_authorization_header
        """
        if not authorization_header or type(authorization_header) != str:
            return None
        if authorization_header[:6] != 'Basic ':
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str) -> str:
        """ decode_base64_authorization_header
        """
        if not base64_authorization_header or type(base64_authorization_header) != str:
            return None
        try:
            return base64.b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None

