from db import init_users, init_recipes

users = init_users()
recipes = init_recipes()

class User(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.role = 'user'


    def is_unique(self):
        return False if users.find_one({'name': self.username}) else True


    def create_user(self):
        users.insert_one(self.to_json())


    def find_user(self):
        return users.find_one({'name': self.username})


    def to_json(self):
        
        return {
            "name": self.username,
            "role": self.role,
            "password": self.password,
        }
    

class Recipe(object):

    def __init__(self, name, user, description, img, meal_type, time, portion, difficulty, ingredients, steps):
        self.name = name
        self.user = user
        self.description = description
        self.img = img
        self.meal_type = meal_type
        self.time = time
        self.portion = portion
        self.difficulty = difficulty
        self.ingredients = ingredients
        self.steps = steps
        self.views = 0


    def add_recipe(self):
        return recipes.insert_one(self.to_json()).inserted_id
    
    def to_json(self):
        return {
            "name": self.name,
            "user": self.user,
            "description": self.description,
            "img": self.img,
            "type": self.meal_type,
            "time": self.time,
            "portion": self.portion,
            "difficulty": self.difficulty,
            "ingredients": self.ingredients,
            "steps": self.steps,
            "views": self.views
        }