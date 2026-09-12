import datetime
import os
from tickex import extractors


class TestYahooExtractor:
    def test_extract(self, df, mock_yfinance, monkeypatch):
        """Test extracting from the YahooExtractor

        :return None:
        :raises AssertionError:
        """
        monkeypatch.setattr(extractors, "yfinance", mock_yfinance)
        extracted_df = extractors.YahooExtractor().extract(
            datetime.datetime.utcnow(),
            datetime.datetime.utcnow(),
            '1d'
        )
        assert len(extracted_df) == len(df) and extracted_df.equals(df)

    def test_get_default_ticker_names(self):
        """test getting some default tickers

        :return None:
        :raises AssertionError:
        """
        assert extractors.YahooExtractor.get_default_ticker_names()

    def test_get_additional_ticker_names_empty(self):
        """test getting additional tickers

        :return None:
        :raises AssertionError:
        """
        additional_ticker_names = extractors.YahooExtractor.get_additional_ticker_names()
        assert isinstance(additional_ticker_names, set) and not additional_ticker_names

    def test_get_additional_ticker_names_not_empty(self):
        """test getting additional tickers

        :return None:
        :raises AssertionError:
        """
        raw_ticker_names = "A,B,C"
        os.environ["ADDITIONAL_TICKERS"] = raw_ticker_names
        additional_ticker_names = extractors.YahooExtractor.get_additional_ticker_names()
        assert isinstance(additional_ticker_names, set) and all(additional_ticker_names)
        assert additional_ticker_names == {"A", "B", "C"}

    def test_get_default_ticker_names_with_additional_tickers(self):
        """test getting some default tickers with additionals

        :return None:
        :raises AssertionError:
        """
        raw_ticker_names = "A,B,C"
        os.environ["ADDITIONAL_TICKERS"] = raw_ticker_names
        names = extractors.YahooExtractor.get_default_ticker_names()
        assert {"A", "B", "C"} & set(names) == {"A", "B", "C"}
    

