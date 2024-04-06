from config import Config
from pymongo import MongoClient

def init_db():

    client = MongoClient(Config.MONGODB_HOST, Config.MONGODB_PORT)
    db = client[Config.MONGODB_NAME]
    
    return db