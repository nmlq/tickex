from tickex import loaders
from tickex import types
import datetime


class TestMongoLoader:
    def test_get_collection_with_mocks(
            self,
            mock_mongo_client_class,
            monkeypatch):
        """Test get collection with mocks

        :return None:
        :raises AssertionError:
        """
        monkeypatch.setattr(loaders, "MongoClient", mock_mongo_client_class)
        loader = loaders.MongoLoader(None, None, None)
        assert loader.get_collection('mock_collection_name')

    def test_get_last_ticker_with_mocks(
            self,
            mock_mongo_client_class,
            monkeypatch):
        """Test get last ticker with mocks

        :return None:
        :raises AssertionError:
        """
        monkeypatch.setattr(loaders, "MongoClient", mock_mongo_client_class)
        loader = loaders.MongoLoader(None, None, None)
        ticker = loader.get_last_ticker('1d')
        assert ticker and isinstance(ticker, types.Ticker)
        assert isinstance(ticker.timestamp, datetime.datetime)

    def test_get_last_ticker_none_with_mocks(
            self,
            mock_mongo_client_class,
            monkeypatch):
        """Test get last ticker (None) with mocks

        :return None:
        :raises AssertionError:
        """
        mock_mongo_client_class.MAX_RESULTS = 0
        monkeypatch.setattr(loaders, "MongoClient", mock_mongo_client_class)
        loader = loaders.MongoLoader(None, None, None)
        ticker = loader.get_last_ticker('1d')
        assert ticker is None
        mock_mongo_client_class.MAX_RESULTS = 1

    def test_load_with_mocks(
            self,
            mock_mongo_client_class,
            monkeypatch,
            ticker_dt):
        """Test load with mocks

        :return None:
        :raises AssertionError:
        """
        monkeypatch.setattr(loaders, "MongoClient", mock_mongo_client_class)
        loader = loaders.MongoLoader(None, None, None)
        assert loader.load([ticker_dt], '1d')
