class User(object):

    def __init__(self, name, email, permissions):
        self.name = name
        self.email = email
        self.permissions = permissions


    def to_json(self):
        
        return {
            "name": self.name,
            "email": self.email,
            "permissions": self.permissions
        }
    