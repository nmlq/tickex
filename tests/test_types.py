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
    """Test getting a dictionary from the Ticker with a datetime

    :return None:
    :raises AssertionError:
    """
    dictionary = ticker.to_dict(dt_enabled=True)
    assert dictionary
    assert isinstance(dictionary['timestamp'], datetime.datetime)


def test_ticker_from_dict(ticker):
    """Test getting a Ticker from a dictionary

    :return None:
    :raises AssertionError:
    """
    dictionary = ticker.to_dict()
    new_ticker = types.Ticker.from_dict(dictionary)
    assert new_ticker and isinstance(
        new_ticker,
        types.Ticker
    ) and isinstance(
        new_ticker.timestamp,
        str
    )
    assert new_ticker == ticker


def test_ticker_from_dict_extra_args(ticker):
    """Test getting a Ticker from a dictionary with extra args

    :return None:
    :raises AssertionError:
    """
    dictionary = ticker.to_dict()
    # Similar to output of a MongoDB instance
    dictionary['_id'] = 1234
    new_ticker = types.Ticker.from_dict(dictionary)
    assert new_ticker and isinstance(
        new_ticker,
        types.Ticker
    ) and isinstance(
        new_ticker.timestamp,
        str
    )
    assert new_ticker == ticker


def test_ticker_from_dict_dt_enabled(ticker_dt):
    """Test getting a Ticker from a dictionary

    :return None:
    :raises AssertionError:
    """
    dictionary = ticker_dt.to_dict(dt_enabled=True)
    new_ticker = types.Ticker.from_dict(dictionary, dt_enabled=True)
    assert new_ticker and isinstance(
        new_ticker,
        types.Ticker
    ) and isinstance(
        new_ticker.timestamp,
        datetime.datetime
    )
    assert new_ticker == ticker_dt
