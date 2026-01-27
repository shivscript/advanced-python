import os

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# MongoDB connection settings
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = os.getenv("DB_NAME", "opportunity_db")

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    # Test the connection
    client.admin.command('ping')
    print(f"✓ Connected to MongoDB at {MONGO_URI}")
except ConnectionFailure as e:
    print(f"✗ Failed to connect to MongoDB: {e}")
    raise

db = client[DB_NAME]

# Collections
jobs_collection = db["jobs"]
courses_collection = db["courses"]