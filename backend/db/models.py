class User(object):

    def __init__(self, name, email, password, permissions):
        self.name = name
        self.email = email
        self.password = password
        self.permissions = permissions


    def to_json(self):
        
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "permissions": self.permissions
        }
    