from config import MongoConfig
from pymongo import MongoClient

db = MongoClient(MongoConfig.MONGODB_HOST, MongoConfig.MONGODB_PORT)[MongoConfig.MONGODB_NAME]

def init_users():
    return db[MongoConfig.MONGODB_USERS]

def init_recipes():
    return db[MongoConfig.MONGODB_RECIPES]