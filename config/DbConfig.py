from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()


def getMongoDBCollection():
    mongo_uri = "mongodb+srv://codesamikshya123:"+os.getenv('MONGODB_PASSWORD')+"@cluster0.6cdggzd.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(mongo_uri)

    # Connect to the database
    db = client[os.getenv('MONGO_DB_NAME')]

    # Define a collection (similar to a table in relational databases)
    collection = db[os.getenv('MONGODB_COLLECTION_NAME')]

    return collection