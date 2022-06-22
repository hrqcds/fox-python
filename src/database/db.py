import os

from dotenv import load_dotenv
from pymongo import MongoClient


def get_host():
    load_dotenv()

    client = MongoClient(os.getenv("database_host"), int(os.getenv("database_port")))

    db = client[os.getenv("database_collection_name")]
    return db

