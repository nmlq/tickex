import datetime
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
