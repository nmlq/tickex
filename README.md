# Tickex

Gather market ticker data and persist to a external source. A ETL pipeline.

## Requirements

When using the mongodb loader (default) with the cli, the following environment variables are required.

* `MONGO_PASS` - Mongo DB password
* `MONGO_URI` - Mongo DB endpoint
* `MONGO_USER` - Mongo DB username
* `MONGO_PROTOCOL` - Mongo DB connection protocol

`MONGO_PROTOCOL` is usually `mongodb` or `mongodb+srv`

Be default, a database called `tickerx` will be created with two collections `1d` and `15m`.

## Pipeline

Using the `yfinance` module, initially get 5 years of single day tickers and 60 days of 15 minute tickers.

If the data is populated in the database, use the last known timestamp to get all new ticker data from the previous date to the present.

## Yahoo Finance Data Format

The yahoo data is exported as a DataFrame which is a good format for testing but for using in a database it needs to be translated into a usable single object.

The data gets translated into the following format.

Example
```
{
  "name": "BNB-USD",
  "timestamp": "2025-01-17T23:12:42.640271+00:00",
  "close": 615.2003784179688,
  "high": 615.2003784179688,
  "low": 615.0079345703125,
  "open": 615.0079345703125,
  "volume": 0.0,
  "interval": "15m"
}
```
