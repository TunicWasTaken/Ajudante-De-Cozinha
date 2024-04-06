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
        user = User(name=user["name"], email=user["email"], permissions=user["permissions"]).to_json()
        user["id"] = _id

        response.append(user)

    return jsonify(response), 201