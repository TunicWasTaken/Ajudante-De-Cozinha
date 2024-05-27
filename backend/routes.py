from __main__ import app, users, recipes
from models import User, Recipe
from hashlib import sha256
from flask import jsonify, request
from datetime import datetime, timedelta, timezone
from flask_jwt_extended import (create_access_token, get_jwt_identity, jwt_required, 
                                unset_jwt_cookies, set_access_cookies, get_jwt)


@app.route("/api/create-user", methods=['POST'])
def create_user():

    data = request.get_json()
    new_user = User(data["username"], sha256(data["password"].encode("utf-8")).hexdigest())

    if not new_user.is_unique():
        return jsonify({"msg": "Username already exists."}), 401
    
    new_user.create_user()

    access_token = create_access_token(identity=data["username"])

    resp = jsonify({'login': True})
    set_access_cookies(resp, access_token)

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

        resp = jsonify({'login': True})
        set_access_cookies(resp, access_token)

        return resp, 201
    
    else:
        return jsonify(message="Unauthorized"), 401

        

@app.route("/api/logout", methods=['GET'])
@jwt_required()
def logout():

    resp = jsonify({'logout': True})
    unset_jwt_cookies(resp)

    return resp, 201


@app.after_request
def refresh_token(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original response
        return response


@app.route("/api/profile", methods=['GET'])
@jwt_required()
def profile():
    username = get_jwt_identity()

    user = dict(users.find_one({'name': username}, {'_id': False}))
    del user['password']

    return user, 201


@app.route("/api/recipe", methods=['POST', 'GET'])
@jwt_required()
def handle_recipe():

    if request.method == 'POST':

        data = request.get_json()

        time = data['time'].split(":")
        time = int(time[0]) * 60 * 60 + int(time[1]) * 60
        
        for step in data['steps']:
            if step['timed']:
                step_time = step['time'].split(":")
                step['time'] = int(step_time[0]) * 60 * 60 + int(step_time[1]) * 60

            else:
                step['timed'] = 0
        
        recipe = Recipe(data['name'], data['user'], data['description'], data['img'], data['type'], 
                        time, data['portion'], data['difficulty'], data['ingredients'], data['steps'])
        
        _id = str(recipe.add_recipe())

        return jsonify({'msg': 'Recipe create successfully', '_id': _id}), 201