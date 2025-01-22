import pytest
import datetime
from tickex import types


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