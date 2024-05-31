from __main__ import app
from bson import ObjectId
from pymongo import ReturnDocument
from db import init_users, init_recipes
from models import User, Recipe
from hashlib import sha256
from flask import jsonify, request
from datetime import datetime, timedelta, timezone
from flask_jwt_extended import (create_access_token, get_jwt_identity, jwt_required, 
                                unset_jwt_cookies, set_access_cookies, get_jwt)


users = init_users()
recipes = init_recipes()

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
    
    else:

        username = get_jwt_identity()

        recipe_list = list(recipes.find({'user': username}))
    
        for recipe in recipe_list:
            recipe["_id"] = str(recipe["_id"])

        return jsonify({'recipes': recipe_list}), 201
    

@app.route("/api/recipe/<id>", methods=['GET'])
def get_recipe(id):

    recipe = dict(recipes.find_one_and_update({'_id': ObjectId(id)}, {'$inc': {'views': 1}}, return_document=ReturnDocument.AFTER))
    del recipe["_id"]

    return jsonify({'recipe': recipe}), 201


def sort_by_views(recipe):
    return recipe["views"]

@app.route("/api/recipes/homepage", methods=['GET'])
def homepage():

    recipe_list_top5 = list(recipes.find().limit(6))
    
    recipe_list_top5.sort(key=sort_by_views, reverse=True)
    
    for recipe in recipe_list_top5:
        recipe["_id"] = str(recipe["_id"])

    
    recipe_list_new = list(recipes.find().sort({'_id': -1}).limit(14))

    for recipe in recipe_list_new:
        recipe["_id"] = str(recipe["_id"])

    return jsonify({'top5': [recipe for recipe in recipe_list_top5], 'new': [recipe for recipe in recipe_list_new]}), 201


@app.route("/api/recipes", methods=['GET'])
def search_recipe():
    
    params = request.query_string.decode()
    name = ""
    query = {}
    alike_recipes = []

    for param in params.split('&'):
        key, value = param.split("=")

        if key == 'q':
            name = value
            continue

        query[key] = value

    recipe_list = list(recipes.find(query).sort({'_id': -1}))

    for recipe in recipe_list:
        recipe["_id"] = str(recipe["_id"])
        if name.lower() in recipe["name"]:
            alike_recipes.append(recipe)

    return jsonify({'recipes': alike_recipes}), 201


@app.route("/api/recipe/delete/<id>", methods=['DELETE'])
@jwt_required()
def delete_recipe(id):

    username = get_jwt_identity()
    role = users.find_one({'name': username})['role']
    recipe = dict(recipes.find_one({'_id': ObjectId(id)}))

    if not recipe:
        return jsonify({'msg': 'Recipe not found'}), 404

    if recipe['user'] != username or role != "admin":
        return jsonify({'msg': 'Unauthorized'}), 401
    
    recipes.delete_one({'_id': ObjectId(id)})
    return jsonify({'msg': 'Recipe deleted'}), 201
