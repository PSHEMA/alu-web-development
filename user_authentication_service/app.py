#!/usr/bin/env python3
""" Flask App
"""

from flask import Flask, jsonify, request, abort
import flask
from auth import Auth

app = Flask(__name__)
auth = Auth()


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    """ POST /users
    Register a new user
    """
    email = flask.request.form.get("email")
    password = flask.request.form.get("password")
    try:
        user = auth.register_user(email, password)
        return flask.jsonify({"email": user.email,
                              "message": "user created"}), 200
    except ValueError:
        return flask.jsonify({"message": "email already registered"}), 400


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """ GET /
    Return:
      - message
    """
    return flask.jsonify({"message": "Bienvenue"})


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login():
    """ Log in """
    email = request.form.get('email')
    password = request.form.get('password')
    if auth.valid_login(email, password) is False:
        abort(401)
    session_id = auth.create_session(email)
    response = jsonify({'email': email, 'message': 'logged in'})
    response.set_cookie('session_id', session_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
