from db import init_db
from config import Config

db = init_db()

def init_users():
    return db[Config.MONGODB_USERS]

def init_recipes():
    return db[Config.MONGODB_RECIPES]