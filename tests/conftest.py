import pytest
import datetime
import pandas
import os
from tickex import types


abspath = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture(scope='session')
def ticker():
    """test ticker for unit tests"""
    return types.Ticker(
        name="USDGBP",
        timestamp=datetime.datetime.now().isoformat(),
        close=1.0,
        high=1.0,
        low=1.0,
        open=1.0,
        volume=1.0,
        interval='15m'
    )

@pytest.fixture(scope='session')
def df(filename="test-ticker-data.pkl"):
    """test dataframe for unit tests"""
    path = f"{abspath}/{filename}"
    return pandas.read_pickle(path)


@pytest.fixture(scope='session')
def mock_yfinance(df):
    class MockYFinance:
        def download(self, *args, **kwargs):
            return df
    return MockYFinance()