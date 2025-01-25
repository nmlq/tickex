from tickex import loaders
from tickex import extractors
from tickex import translators
from tickex import pipeline
import datetime
import pytest


class TestPipeline:
    # TODO; Additional tests; ticker none and interval changes
    def test_run_with_mocks(
            self,
            monkeypatch,
            mock_mongo_client_class,
            mock_yfinance):
        """Test run the pipeline with mocks

        :return None:
        :raises AssertionError:
        """
        monkeypatch.setattr(loaders, "MongoClient", mock_mongo_client_class)
        monkeypatch.setattr(extractors, "yfinance", mock_yfinance)
        assert pipeline.Pipeline(
            extractor=extractors.YahooExtractor(),
            translator=translators.YahooTranslator(),
            loader=loaders.MongoLoader(None, None, None)
        ).run()

    def test_get_start_date_with_ticker(
            self,
            monkeypatch,
            mock_mongo_client_class,
            mock_yfinance):
        """Test run the pipeline with mocks

        :return None:
        :raises AssertionError:
        """
        monkeypatch.setattr(loaders, "MongoClient", mock_mongo_client_class)
        monkeypatch.setattr(extractors, "yfinance", mock_yfinance)
        dt = pipeline.Pipeline(
            extractor=extractors.YahooExtractor(),
            translator=translators.YahooTranslator(),
            loader=loaders.MongoLoader(None, None, None)
        ).get_start_date('1d')
        assert dt and isinstance(dt, datetime.datetime)

    def test_get_start_date_none_ticker_1d(
            self,
            ticker_dt,
            monkeypatch,
            mock_mongo_client_class,
            mock_yfinance):
        """Test run the pipeline with mocks, None ticker results for 1d

        :return None:
        :raises AssertionError:
        """
        mock_mongo_client_class.MAX_RESULTS = 0
        monkeypatch.setattr(loaders, "MongoClient", mock_mongo_client_class)
        monkeypatch.setattr(extractors, "yfinance", mock_yfinance)
        dt = pipeline.Pipeline(
            extractor=extractors.YahooExtractor(),
            translator=translators.YahooTranslator(),
            loader=loaders.MongoLoader(None, None, None)
        ).get_start_date('1d')
        assert dt and isinstance(dt, datetime.datetime)
        # dt object should be in past, no collection, tries to create it
        assert ticker_dt.timestamp > dt
        mock_mongo_client_class.MAX_RESULTS = 1

    def test_get_start_date_none_ticker_15m(
            self,
            ticker_dt,
            monkeypatch,
            mock_mongo_client_class,
            mock_yfinance):
        """Test run the pipeline with mocks, None ticker results for 15m

        :return None:
        :raises AssertionError:
        """
        mock_mongo_client_class.MAX_RESULTS = 0
        monkeypatch.setattr(loaders, "MongoClient", mock_mongo_client_class)
        monkeypatch.setattr(extractors, "yfinance", mock_yfinance)
        dt = pipeline.Pipeline(
            extractor=extractors.YahooExtractor(),
            translator=translators.YahooTranslator(),
            loader=loaders.MongoLoader(None, None, None)
        ).get_start_date('15m')
        assert dt and isinstance(dt, datetime.datetime)
        # dt object should be in past, no collection, tries to create it
        assert ticker_dt.timestamp > dt
        mock_mongo_client_class.MAX_RESULTS = 1

    def test_get_start_date_none_ticker_unsupported_interval(
            self,
            monkeypatch,
            mock_mongo_client_class,
            mock_yfinance):
        """Test run the pipeline with mocks, None ticker results for 15m

        :return None:
        :raises AssertionError:
        """
        mock_mongo_client_class.MAX_RESULTS = 0
        monkeypatch.setattr(loaders, "MongoClient", mock_mongo_client_class)
        monkeypatch.setattr(extractors, "yfinance", mock_yfinance)
        with pytest.raises(Exception):
            pipeline.Pipeline(
                extractor=extractors.YahooExtractor(),
                translator=translators.YahooTranslator(),
                loader=loaders.MongoLoader(None, None, None)
            ).get_start_date('unsupported')
        mock_mongo_client_class.MAX_RESULTS = 1
