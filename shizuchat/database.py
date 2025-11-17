# database.py
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
import config

motor = AsyncIOMotorClient(config.MONGO_URL)
mongodb = motor.Anonymous

mongo = MongoClient(config.MONGO_URL)
sync_db = mongo.Anonymous
