#!/usr/bin/env python3
""" Session Authentication
"""
from flask import app, jsonify, request
from api.v1.auth.auth import Auth
from models.user import User


@app.views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /api/v1/auth_session/login
    Return:
      - session ID
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or email == "" or password is None or password == "":
        return jsonify({"error": "email and password are required"}), 400

    try:
        user = User.search({'email': email})[0]
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = Auth().create_session(user.id)

    return jsonify({"user_id": user.id, "session_id": session_id})
