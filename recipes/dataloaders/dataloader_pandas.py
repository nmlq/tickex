"""Loads Tickers into a Pandas DataFrame"""
from __future__ import annotations

from datetime import datetime, timedelta
from pandas import DataFrame


import pandas as pd
import logging

from recipes.dataloaders import DataLoaderBase

logger = logging.getLogger(__name__)


class PandasLoader(DataLoaderBase):
    def query_collection(
            self,
            start_time: datetime | None = None,
            end_time: datetime | None = None,
            time_delay: float = 0.,
            interval: str = '1d'
    ) -> DataFrame :
        """
        Query Collection and return Pandas DataFrame
        :param start_time: initial datetime to search from. If None, `time_delta` is used.
        :param end_time: end time to search to. If None, it searches till NOW()
        :param time_delay: time to delay between requests. If None, no delay.
            if `start_time` is given, `time_delay` is ignored.
        :param interval: `1d` or `15m`
        :return: pandas.DataFrame
        """
        results = super().query_collection(
            start_time=start_time,
            end_time=end_time,
            time_delay=time_delay,
            interval=interval
        )

        # Convert cursor to a list
        results = list(results)
        # Convert to Pandas DataFrame
        df = pd.DataFrame(results)

        # Optional: Drop MongoDB's `_id` field if not needed
        if "_id" in df.columns:
            df.drop(columns=["_id"], inplace=True)

        # Drop NaN
        df.dropna(inplace=True,ignore_index=True)
        return df


if __name__ == "__main__":
    loader = PandasLoader()
    df = loader.query_collection(
        time_delay=1,
    )
    print(len(df))

