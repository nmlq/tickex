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
