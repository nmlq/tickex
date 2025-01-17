from tickex import types
import yfinance
import datetime


def get_default_ticker_names():
    return [
        ### Fiat currency
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
        ### Crypto currency
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


def get_tickers(
        start_date: datetime.datetime,
        end_date: datetime.datetime,
        interval: str,
        ticker_names: list = None) -> list[types.Ticker]:
    """Get all the tickers

    :returns list:
    """
    if not ticker_names:
        ticker_names = get_default_ticker_names()

    df = yfinance.download(ticker_names, start_date, end_date, interval=interval)
    tickers = []
    for timestamp, row in df.iterrows():
        for ticker_name, ticker_values in row.groupby('Ticker'):
            ticker = types.Ticker(
                name = ticker_name,
                # Can convert back into timestamp using datetime.datetime.fromisoformat
                timestamp = timestamp.utcnow().isoformat(),
                close = float(ticker_values[('Close', ticker_name)]),
                high = float(ticker_values[('High', ticker_name)]),
                low = float(ticker_values[('Low', ticker_name)]),
                open = float(ticker_values[('Open', ticker_name)]),
                volume = float(ticker_values[('Volume', ticker_name)]),
                interval = interval
            )
            tickers.append(ticker)
    return tickers