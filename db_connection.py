import pymongo
from django.conf import settings

url = settings.MONGODB_CONNECTION_STRING
client = pymongo.MongoClient(url)


db = client.rentopia_db
