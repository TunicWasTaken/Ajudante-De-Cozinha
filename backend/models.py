from db import init_users, init_recipes

class User(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.role = 'user'
        self.users = init_users()


    def is_unique(self):
        return False if self.users.find_one({'name': self.username}) else True


    def create_user(self):
        self.users.insert_one(self.to_json())


    def find_user(self):
        return self.users.find_one({'name': self.username})


    def to_json(self):
        
        return {
            "name": self.username,
            "role": self.role,
            "password": self.password,
        }