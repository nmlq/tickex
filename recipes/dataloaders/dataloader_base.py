from __future__ import annotations

from pymongo.synchronous.collection import Collection
from datetime import datetime, timedelta

from tickex.loaders import MongoLoader
from tickex.cli import validate_envvars

import os


class DataLoaderBase:
    def __init__(self):
        validate_envvars()
        self.loader = MongoLoader(
            user=os.environ['MONGO_USER'],
            password=os.environ['MONGO_PASS'],
            uri=os.environ['MONGO_URI']
        )

    def query_collection(
        self,
        start_time: datetime | None = None,
        end_time: datetime | None = None,
        time_delay: float = 0.,
        interval: str = '1d'
    ) -> Collection:
        collection = self.loader.get_collection(interval)
        if end_time is None:
            end_time = datetime.utcnow()

        if start_time is None:
            if time_delay <= 0:
                raise ValueError(
                    "If `start_time` is None, `time_delay` must be greater than 0.")
            start_time = end_time - timedelta(days=time_delay)

        query = {
            "timestamp": {"$gte": start_time, "$lte": end_time}
        }
        # Retrieve data from MongoDB
        return collection.find(query)
