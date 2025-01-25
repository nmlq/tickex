import logging
import pandas
from tickex import types

logger = logging.getLogger(__name__)


class YahooTranslator:
    def translate(
            self,
            df: pandas.DataFrame,
            interval: str) -> list[types.Ticker]:
        """Translate the dataframe to a list of tickers

        :return list: list of Ticker objects
        """
        logger.info(
            f"Translating {len(df)} rows to Tickers for interval {interval}"
        )
        tickers = []
        for timestamp, row in df.iterrows():
            for ticker_name, ticker_values in row.groupby('Ticker'):
                ticker = types.Ticker(
                    name=ticker_name,
                    timestamp=timestamp.utcnow().isoformat(),
                    close=float(ticker_values[('Close', ticker_name)]),
                    high=float(ticker_values[('High', ticker_name)]),
                    low=float(ticker_values[('Low', ticker_name)]),
                    open=float(ticker_values[('Open', ticker_name)]),
                    volume=float(ticker_values[('Volume', ticker_name)]),
                    interval=interval
                )
                tickers.append(ticker)
        logger.info(
            f"Translated {len(tickers)} tickers for interval {interval}"
        )
        return tickers
