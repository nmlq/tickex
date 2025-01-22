import os
import pymongo
import logging


logger = logging.getLogger(__name__)


def get_connection_string() -> str:
    """Get the connection string from the environment variables

    :return str:
    """
    user = os.environ['MONGO_USER']
    password = os.environ['MONGO_PASS']
    uri = os.environ['MONGO_URI']
    return f"mongodb+srv://{user}:{password}@{uri}"


def get_client() -> pymongo.MongoClient:
    """Get a database client.

    :return MongoClient:
    """
    return pymongo.MongoClient(
        get_connection_string()
    )


def get_database(
        name: str = "tickex") -> pymongo.synchronous.database.Database:
    """Get the default database

    :return
    """
    client = get_client()
    database = client.get_database(name)
    return database


def get_collection(name: str) -> pymongo.synchronous.collection.Collection:
    """Return the collection by the name.

    If it doesnt exist make it.

    :return Collection:
    """
    timeseries = {
        "timeField": "timestamp"
    }
    database = get_database()
    collection_names = database.list_collection_names()
    if name not in collection_names:
        logger.info(f"Making collection name; {name}")
        database.create_collection(name, timeseries=timeseries)
    collection = database[name]
    return collection
