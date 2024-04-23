from pymongo import MongoClient
from dynaconf import settings

print(f'mongo { settings.get('MONGO_URI')}')
mongo = MongoClient(settings.get('MONGO_URI'))