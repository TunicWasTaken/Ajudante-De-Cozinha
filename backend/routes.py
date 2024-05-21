from __main__ import app
from models import User
from db import init_users
from hashlib import sha256
from flask import jsonify, request
from datetime import datetime, timedelta, timezone
from flask_jwt_extended import (create_access_token, create_refresh_token, 
                                get_jwt_identity, jwt_required, 
                                unset_jwt_cookies, set_access_cookies, 
                                set_refresh_cookies, get_jwt)


users = init_users()

@app.route("/api/create-user", methods=['POST'])
def create_user():

    data = request.get_json()
    new_user = User(data["username"], sha256(data["password"].encode("utf-8")).hexdigest())

    if not new_user.is_unique():
        return jsonify({"msg": "Username already exists."}), 401
    
    new_user.create_user()

    access_token = create_access_token(identity=data["username"])
    refresh_token = create_refresh_token(identity=data["username"])

    resp = jsonify({'login': True})
    set_access_cookies(resp, access_token)
    set_refresh_cookies(resp, refresh_token)

    return resp, 201


@app.route("/api/login", methods=['POST'])
def login():

    data = request.get_json()

    username = data["username"]
    password = sha256(data["password"].encode("utf-8")).hexdigest()

    user = User(username, password).find_user()

    if user:
        if user["password"] != password:
            return jsonify(message="Unauthorized"), 401
        
        access_token = create_access_token(identity=username)
        refresh_token = create_refresh_token(identity=username)

        resp = jsonify({'login': True})
        set_access_cookies(resp, access_token)
        set_refresh_cookies(resp, refresh_token)

        return resp, 201
    
    else:
        return jsonify(message="Unauthorized"), 401

        

@app.route("/api/logout", methods=['GET'])
@jwt_required()
def logout():

    resp = jsonify({'logout': True})
    unset_jwt_cookies(resp)

    return resp, 201



@app.route("/api/refresh", methods=['POST'])
@jwt_required(refresh=True)
def refresh():

    username = get_jwt_identity()
    access_token = create_access_token(identity=username)

    resp = jsonify({'refresh': True})
    set_access_cookies(resp, access_token)

    return resp, 201


@app.route("/api/profile", methods=['GET'])
@jwt_required()
def profile():
    username = get_jwt_identity()

    user = dict(users.find_one({'name': username}, {'_id': False}))
    del user['password']

    return user, 201


@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target = datetime.timestamp(now + timedelta(hours=22))

        if target > exp:
            access_token = create_access_token(identity=get_jwt_identity())

            set_access_cookies(response, access_token)

        return response
    
    except (RuntimeError, KeyError):
        return response