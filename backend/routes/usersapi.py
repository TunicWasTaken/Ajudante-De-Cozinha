from bson.json_util import dumps
from flask import current_app, jsonify, request
from db.models import User
from . import init_users

users = init_users()

@current_app.route("/api", methods=['GET', 'POST'])
def index():
    return "Hello World!"


@current_app.route("/api/users", methods=['GET'])
def get_users():

    user_list = list(users.find({}))
    response = []

    for user in user_list:
        _id = str(user["_id"])
        user = User(name=user["name"], email=user["email"], password=user["password"]).to_json()
        user["id"] = _id

        response.append(user)

    return jsonify(response), 201


@current_app.route("/api/create_user", methods=['POST'])
def create_user():

    req = request.get_json()
    new_user = User(name=req["username"],
                    email=req["email"], 
                    password=req["password"])
        

    if users.find_one({'email': req["email"]}):
        return "email", 400
    
    if users.find_one({'name': req["username"]}):
        return "username", 400
    

    
    res = users.insert_one(new_user.to_json())

    return jsonify(str(res.inserted_id)), 201