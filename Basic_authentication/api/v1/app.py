#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None

# Instantiate the correct auth method based on the environment variable
if os.getenv("AUTH_TYPE") == "auth":
    auth = Auth()
elif os.getenv("AUTH_TYPE") == "basic_auth":
    auth = BasicAuth()

@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403

@app.before_request
def before_request() -> str:
    """ Before request handler
    """
    # If no auth method is set, bypass authentication
    if auth is None:
        return

    # Define paths that don't require authentication
    excluded_paths = ["/api/v1/status/", "/api/v1/unauthorized/", "/api/v1/forbidden/"]

    # If the current path doesn't require authentication, return without aborting
    if not auth.require_auth(request.path, excluded_paths):
        return

    # Abort with a 401 error if the authorization header is missing
    if auth.authorization_header(request) is None:
        abort(401)

    # Abort with a 403 error if the current user cannot be determined
    if auth.current_user(request) is None:
        abort(403)

    # Allow the request to proceed if everything is fine
    return None  # Return `None` explicitly to avoid undefined return types

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
