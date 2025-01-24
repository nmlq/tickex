from tickex import types
import yfinance
import datetime
import pandas
import logging


logger = logging.getLogger(__name__)


class YahooExtractor:
    """Extract ticker data from yahoo finanace"""
    def __init__(self, ticker_names: list|None = None):
        self.ticker_names = ticker_names
        if ticker_names is None:
            self.ticker_names = self.get_default_ticker_names()
        logger.info(f"Initialized extractor with {len(self.ticker_names)} ticker names; {self.ticker_names}")

    def get_default_ticker_names(self) -> list:
        """Default supported tickers

        :return list:
        """
        return [
            # Fiat currency
            # US Dollar / Pound Sterling
            "USDGBP=X",
            # US Dollar / Euro
            "USDEUR=X",
            # US Dollar / Yen
            "USDJPY=X",
            # US Dollar / Canadian Dollar
            "USDCAD=X",
            # US Dollar / Mexican Peso
            "USDMXN=X",
            # US Dollar / Chilean Peso
            "USDCLP=X",
            # US Dollar / Brazilian Real
            "USDBRL=X",
            # Crypto currency
            # US Dollar / Bitcoin
            "BTC-USD",
            # US Dollar / Ethereum
            "ETH-USD",
            # US Dollar / BNB Chain
            "BNB-USD",
            # US Dollar / Tether
            "USDT-USD",
            # US Dollar / Solana
            "SOL-USD",
            # US Dollar / Dogecoin
            "DOGE-USD"
        ]

    def extract(
            self,
            start_date: datetime.datetime,
            end_date: datetime.datetime,
            interval: str) -> pandas.DataFrame:
        """Get all the tickers

        :returns list:
        """
        logger.info(f"Extracting {interval} interval from {start_date} to {end_date}")
        df = yfinance.download(
            self.ticker_names,
            start_date,
            end_date,
            interval=interval
        )
        logger.info(f"Extracted {len(df)} rows from yfinance")
        return df
