from datetime import timedelta

class MongoConfig():
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27017
    MONGODB_NAME = 'Ajudante_De_Cozinha'
    MONGODB_USERS = 'Users'
    MONGODB_RECIPES = 'Recipes'


class AppConfig():
    JWT_SECRET_KEY = 'very-secret'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    JWT_COOKIE_SECURE = False
    JWT_TOKEN_LOCATION = ['cookies']