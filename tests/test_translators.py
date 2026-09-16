from tickex import translators
from tickex import types


class TestYahooTranslator:
    def test_translate(self, df):
        """Test translating to ticker objects"""
        tickers = translators.YahooTranslator().translate(df, interval='1d')
        assert tickers and all([
            isinstance(ticker, types.Ticker)
            for ticker in tickers
        ])

    def test_translate_differing_timestamps(self, df):
        """Test translating to ticker objects

        ensure the timestamps are different

        :return None:
        :raises AssertionError:
        """
        tickers = translators.YahooTranslator().translate(df, interval='1d')
        timestamps = set([t.timestamp for t in tickers])
        assert len(timestamps) > 1
