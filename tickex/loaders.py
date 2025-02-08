from __future__ import annotations

from pymongo import MongoClient
import pymongo
import datetime
import logging
from tickex import types


logger = logging.getLogger(__name__)


class MongoLoader:
    """Load the tickers into a mongo db database"""
    def __init__(
            self,
            user: str,
            password: str,
            uri: str,
            database_name: str = 'tickex',
            local_host: bool = True) -> None:
        """

        :param user:
        :param password:
        :param uri:
        :param database_name:
        :param local_host: Indicates if it's running locally or MongoDB Atlas Cloud service
        """

        host = 'mongodb+srv'
        if local_host:
            host = 'mongodb'
        self.connection_string = f"{host}://{user}:{password}@{uri}"
        self.client = MongoClient(self.connection_string)
        self.database = self.client.get_database(database_name)

    def get_last_ticker(
            self,
            collection_name: str) -> datetime.datetime | None:
        """Get the last timestamp for the collection

        If the collection does not exist, return None

        :return datetime | None:
        """
        if collection_name not in self.database.list_collection_names():
            logger.info("Collection unknown; cannot extract timestamp")
            return None
        collection = self.get_collection(collection_name)
        results = list(collection.find().sort({'timestamp': -1}).limit(1))
        if not results or len(results) < 1:
            return None
        last, *_ = results
        return types.Ticker.from_dict(last, dt_enabled=True)

    def get_collection(
            self,
            collection_name: str) -> pymongo.synchronous.collection.Collection:
        """Return the collection by the name.

        If it doesnt exist make it.

        :return Collection:
        """
        timeseries = {
            "timeField": "timestamp"
        }
        collection_names = self.database.list_collection_names()
        if collection_name not in collection_names:
            logger.info(f"Making collection name; {collection_name}")
            self.database.create_collection(
                collection_name,
                timeseries=timeseries
            )
        collection = self.database[collection_name]
        return collection

    def load(self, tickers: list[types.Ticker], interval: str) -> bool:
        """Load the ticker data into the database

        :return bool: true on success
        """
        logger.info(f"Loading {len(tickers)} tickers for interval {interval}")
        dictionaries = [t.to_dict(dt_enabled=True) for t in tickers]
        collection = self.get_collection(interval)
        logger.info(f"Got {collection} insert {len(dictionaries)} dicts")
        return collection.insert_many(dictionaries).acknowledged
