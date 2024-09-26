#!/usr/bin/env python3
""" Flask App
"""

from flask import Flask
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
def login() -> str:
    """ POST /sessions
    Login
    """
    email = flask.request.form.get("email")
    password = flask.request.form.get("password")
    if email is None or email == "":
        return flask.jsonify({"error": "email missing"}), 400
    if password is None or password == "":
        return flask.jsonify({"error": "password missing"}), 400
    try:
        user = auth.valid_login(email, password)
        if user is False:
            return flask.jsonify({"error": "no user found for this email"}), 404
        session_id = auth.create_session(user.id)
        return flask.jsonify({"email": user.email,
                              "message": "logged in",
                              "session_id": session_id}), 200
    except ValueError:
        return flask.jsonify({"error": "wrong password"}), 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
