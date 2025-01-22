from tickex import types
import datetime


def test_ticker_to_dict(ticker):
    """Test getting a dictionary datatype from the Ticker

    :return None:
    :raises AssertionError:
    """
    dictionary = ticker.to_dict()
    assert dictionary
    assert isinstance(dictionary['timestamp'], str)


def test_ticker_to_dict_dt_enabled(ticker):
    """Test getting a dictionary datatype from the Ticker with a datetime timestamp

    :return None:
    :raises AssertionError:
    """
    dictionary = ticker.to_dict(dt_enabled=True)
    assert dictionary
    assert isinstance(dictionary['timestamp'], datetime.datetime)